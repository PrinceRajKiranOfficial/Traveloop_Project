// Auto-dismiss flash messages
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.alert').forEach(el => {
    setTimeout(() => { el.style.opacity = '0'; el.style.transform = 'translateX(20px)'; el.style.transition = 'all .4s'; setTimeout(() => el.remove(), 400); }, 4000);
  });

  // Tab switcher
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const pane = document.getElementById(target);
      if (pane) pane.classList.add('active');
    });
  });

  // Confirm delete — listen on the FORM submit, not the button click
  document.querySelectorAll('form[data-confirm], button[data-confirm]').forEach(el => {
    const target = el.tagName === 'BUTTON' ? el.closest('form') : el;
    if (!target) return;
    target.addEventListener('submit', e => {
      const msg = el.dataset.confirm || target.dataset.confirm || 'Are you sure?';
      if (!confirm(msg)) e.preventDefault();
    });
  });

  // Also handle standalone buttons with data-confirm that are NOT submit buttons
  document.querySelectorAll('[data-confirm]:not(form)').forEach(btn => {
    if (btn.tagName === 'BUTTON' && btn.type === 'submit') return; // handled above via form
    btn.addEventListener('click', e => {
      if (!confirm(btn.dataset.confirm)) e.preventDefault();
    });
  });

  // Drag-to-reorder stops
  initDragSort();
});

function initDragSort() {
  const list = document.getElementById('stops-list');
  if (!list) return;
  let dragging = null;

  list.querySelectorAll('.stop-card').forEach(card => {
    card.setAttribute('draggable', true);
    card.addEventListener('dragstart', () => { dragging = card; card.style.opacity = '.4'; });
    card.addEventListener('dragend', () => { dragging = null; card.style.opacity = '1'; saveOrder(list); });
    card.addEventListener('dragover', e => { e.preventDefault(); if (dragging && dragging !== card) { const r = card.getBoundingClientRect(); const mid = r.top + r.height / 2; list.insertBefore(dragging, e.clientY < mid ? card : card.nextSibling); } });
  });
}

function saveOrder(list) {
  const tripId = list.dataset.tripId;
  if (!tripId) return;
  const order = [...list.querySelectorAll('.stop-card')].map(c => parseInt(c.dataset.stopId));
  fetch(`/trips/${tripId}/stops/reorder`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCSRF() },
    body: JSON.stringify({ order })
  });
}

function getCSRF() {
  return document.querySelector('meta[name="csrf-token"]')?.content || '';
}

// Budget chart initializer
function initBudgetCharts(data) {
  const pieCtx = document.getElementById('budgetPie');
  const barCtx = document.getElementById('budgetBar');
  const labels = ['Transport', 'Stay', 'Activities', 'Meals', 'Misc'];
  const values = [data.transport, data.stay, data.activities, data.meals, data.misc];
  const colors = ['#6366f1','#10b981','#f59e0b','#f43f5e','#8b5cf6'];

  if (pieCtx) {
    new Chart(pieCtx, {
      type: 'doughnut',
      data: { labels, datasets: [{ data: values, backgroundColor: colors, borderWidth: 0, hoverOffset: 8 }] },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { position: 'bottom', labels: { color: '#94a3b8', padding: 16, font: { family: 'Inter' } } },
          tooltip: { callbacks: { label: ctx => ` ₹${ctx.parsed.toFixed(0)}` } }
        },
        cutout: '70%'
      }
    });
  }

  if (barCtx) {
    new Chart(barCtx, {
      type: 'bar',
      data: { labels, datasets: [{ label: 'Amount (₹)', data: values, backgroundColor: colors, borderRadius: 8, borderSkipped: false }] },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: { ticks: { color: '#94a3b8' }, grid: { display: false } },
          y: { ticks: { color: '#94a3b8', callback: v => '₹' + v }, grid: { color: 'rgba(255,255,255,0.05)' } }
        }
      }
    });
  }
}
