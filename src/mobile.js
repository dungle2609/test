/* =====================================================================
   ENGINE MOBILE — đọc dọc. Hiệu ứng giữ đúng thông số deck:
   • .rv trồi lên so le khi phần (slide) đi vào màn hình.
   • [data-step] hiện lần lượt theo số bước khi tới vị trí; dòng mới nhất có class "now" (kết cộng dồn).
   • [data-cls] bật class theo bước khi phần đi vào màn hình (vd. cờ "chưa ai trả lời").
   • Giảm chuyển động: hiện ngay trạng thái cuối.
   ===================================================================== */
(function(){
'use strict';
var REDUCE=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var secs=[].slice.call(document.querySelectorAll('#stage > .slide')), N=secs.length;
function pad(n){return String(n).padStart(2,'0')}
function esc(t){return String(t||'').replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function clsPairs(e){return e.dataset.cls.split(/\s+/).map(function(p){var m=p.split(':');return m.length===2?[+m[0],m[1]]:null}).filter(Boolean)}
secs.forEach(function(s,i){s.id='s'+(i+1)});

function activate(s){
  if(!s||s.classList.contains('is-active'))return;
  s.classList.add('is-active');
  [].slice.call(s.querySelectorAll('[data-cls]')).forEach(function(e){clsPairs(e).forEach(function(p){
    if(REDUCE)e.classList.add(p[1]);else setTimeout(function(){e.classList.add(p[1])},600+p[0]*450)})});
}
function rank(e){var s=e.closest('.slide');return secs.indexOf(s)*1000+(+e.dataset.step||0)}
var queue=[],timer=null;
function show(e){
  var s=e.closest('.slide');
  [].slice.call(s.querySelectorAll('[data-step].now')).forEach(function(x){x.classList.remove('now')});
  e.classList.add('on','now');
}
function flush(){if(!queue.length){timer=null;return}queue.sort(function(a,b){return rank(a)-rank(b)});show(queue.shift());timer=setTimeout(flush,REDUCE?0:240)}

if(!('IntersectionObserver' in window)){secs.forEach(activate);document.querySelectorAll('#stage [data-step]').forEach(show)}
else{
  var ioS=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){activate(en.target);ioS.unobserve(en.target)}})},{rootMargin:'0px 0px -12% 0px',threshold:0});
  var ioE=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;ioE.unobserve(en.target);activate(en.target.closest('.slide'));
    queue.push(en.target);if(!timer)timer=setTimeout(flush,REDUCE?0:280)})},{rootMargin:'0px 0px -14% 0px',threshold:0.12});
  secs.forEach(function(s){ioS.observe(s)});
  document.querySelectorAll('#stage [data-step]').forEach(function(e){ioE.observe(e)});
}
activate(secs[0]);

/* thanh trên cùng: tên phần đang đọc, số thứ tự, tiến độ */
var ttl=document.getElementById('mttl'),cnt=document.getElementById('mcnt'),bar=document.getElementById('mbar'),list=document.getElementById('mlist'),btn=document.getElementById('mtoc'),cur=-1,ticking=false;
function onScroll(){ticking=false;var y=innerHeight*0.35,idx=0;
  for(var i=0;i<N;i++){if(secs[i].getBoundingClientRect().top<=y)idx=i;else break}
  if(idx!==cur){cur=idx;ttl.textContent=secs[idx].dataset.title||'';cnt.textContent=pad(idx+1)+' / '+pad(N);
    [].slice.call(list.querySelectorAll('a')).forEach(function(a,n){a.classList.toggle('cur',n===idx)})}
  var h=document.documentElement.scrollHeight-innerHeight;bar.style.width=(h>0?Math.min(100,Math.max(0,scrollY/h*100)):0)+'%'}
addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
addEventListener('resize',onScroll);

/* mục lục */
list.innerHTML=secs.map(function(s,i){return '<a href="#s'+(i+1)+'"><em>'+pad(i+1)+'</em><span>'+esc(s.dataset.title)+'</span></a>'}).join('');
btn.addEventListener('click',function(){list.hidden=!list.hidden;btn.setAttribute('aria-expanded',String(!list.hidden))});
list.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;e.preventDefault();list.hidden=true;btn.setAttribute('aria-expanded','false');
  var t=document.getElementById(a.getAttribute('href').slice(1));activate(t);t.scrollIntoView({behavior:REDUCE?'auto':'smooth',block:'start'})});
onScroll();
window.__mobile={state:function(){return {cur:cur+1,total:N,shown:document.querySelectorAll('#stage [data-step].on').length,steps:document.querySelectorAll('#stage [data-step]').length}}};
})();
