/* =====================================================================
   ENGINE MOBILE — đọc dọc, hiệu ứng thiết kế riêng cho điện thoại:
   • Mỗi khối hiện khi cuộn tới (nhanh, không nhoè), khối vào cùng lúc thì so le.
   • Mỗi loại nội dung một kiểu: thẻ trồi lên, dòng danh sách trượt từ trái, mảnh Zalo/Excel/email trượt vào
     như thông báo, cờ cảnh báo bật lên; số liệu đếm lên; thanh 90,5% tự đầy; các bước sáng lần lượt.
   • Câu kết sáng theo vị trí cuộn; số chương lớn trôi nhẹ.
   • Giảm chuyển động: hiện ngay trạng thái cuối.
   ===================================================================== */
(function(){
'use strict';
var REDUCE=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var secs=[].slice.call(document.querySelectorAll('#stage > .slide')), N=secs.length;
function pad(n){return String(n).padStart(2,'0')}
function esc(t){return String(t||'').replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function $$(s,r){return [].slice.call((r||document).querySelectorAll(s))}
secs.forEach(function(s,i){s.id='s'+(i+1)});
$$('.mess').forEach(function(m){m.classList.add('loud')});

/* ---------- khối cần hiện và kiểu chuyển động ---------- */
var GROUPS=[
  ['up','.slide > .eyebrow,.slide > h1,.slide > h2,.slide > .sub,.slide > .small,.slide > .lede,.slide > .qline,.slide > .chsum,.slide > .band,.slide > .loop,.slide > .also,.slide > .srcline,.slide > .tagline,.slide > .mcue,.cards > .card,.kpis > .kpi,.meter > .cap0,.meter > .barx,.meter .nt,.versus > .vcol,.lanes > .lane,.chain > .cn,.rules > .rule,.story > .id,.duo > .dcol,.scope > .sc,.arch > .ly,.mp > .mrow,.slide > .refs'],
  ['left','.mx > .r,.stk > .r,.ops > .op,.quotes > .quote,.jr > .jc,.story .bd > *'],
  ['swingL','.mess > .zl,.mess > .ml'],
  ['swingR','.mess > .xl,.mess > .pp'],
  ['drop','.mess > .note'],
  ['pop','.mess > .flag']
];
var targets=[];
GROUPS.forEach(function(g){$$(g[1].split(',').map(function(x){return '#stage '+x.trim()}).join(',')).forEach(function(el){
  if(el.classList.contains('mr'))return;el.classList.add('mr');el.dataset.mv=g[0];targets.push(el)})});
$$('#stage .lane').forEach(function(l){$$('.st',l).forEach(function(st,i){st.style.setProperty('--si',i)})});
$$('#stage .zl,#stage .ml').forEach(function(w){$$('.m,.it',w).forEach(function(b,i){b.style.setProperty('--bi',i)})});

/* ---------- số liệu đếm lên: chỉ số dạng 16,8% · −15% · +65% · 12.000+ ---------- */
var NUM=/^([+−-]?)(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d+))?(%|\+)$/;
function fmt(v,dec,thou){var s=v.toFixed(dec).split('.'),i=s[0];if(thou)i=i.replace(/\B(?=(\d{3})+(?!\d))/g,'.');return i+(dec?','+s[1]:'')}
function countUp(el){
  var txt=el.textContent.trim(),m=NUM.exec(txt);if(!m||REDUCE)return;
  var dec=m[3]?m[3].length:0,to=parseFloat(m[2].replace(/\./g,'')+(dec?'.'+m[3]:'')),thou=m[2].indexOf('.')>=0,t0=null,ms=950;
  el.textContent=m[1]+fmt(0,dec,thou)+m[4];
  function f(now){if(t0===null)t0=now;var k=Math.min(1,(now-t0)/ms),e=1-Math.pow(1-k,3);
    el.textContent=k<1?m[1]+fmt(to*e,dec,thou)+m[4]:txt;if(k<1)requestAnimationFrame(f)}
  setTimeout(function(){requestAnimationFrame(f)},180);
}
var COUNT='.kpi b,.story .id .big,.meter .nt b,.meter .seg.a em';

function reveal(el,delay){
  el.style.setProperty('--md',(delay||0)+'ms');
  el.classList.remove('mr-pending');el.classList.add('mr-in');
  (el.matches(COUNT)?[el]:$$(COUNT,el)).forEach(countUp);
}

if(REDUCE||!('IntersectionObserver' in window)){targets.forEach(function(el){el.classList.add('mr-in')})}
else{
  var vh=innerHeight;
  targets.forEach(function(el){var r=el.getBoundingClientRect();if(r.bottom<0)el.classList.add('mr-in');else el.classList.add('mr-pending')});
  var io=new IntersectionObserver(function(es){
    var ins=es.filter(function(e){return e.isIntersecting}).map(function(e){return e.target});
    ins.sort(function(a,b){return a.compareDocumentPosition(b)&Node.DOCUMENT_POSITION_FOLLOWING?-1:1});
    ins.forEach(function(el,i){io.unobserve(el);reveal(el,Math.min(i,6)*70)});
  },{rootMargin:'0px 0px -8% 0px',threshold:0.06});
  targets.forEach(function(el){if(el.classList.contains('mr-pending'))io.observe(el)});
}

/* ---------- câu kết sáng theo vị trí cuộn; số chương trôi nhẹ ---------- */
var stackLines=$$('#stage .stack p'), ghosts=$$('#stage .ghost');
if(REDUCE)stackLines.forEach(function(p){p.classList.add(p.classList.contains('final')?'now':'past')});
function scrollFx(){
  if(!REDUCE&&stackLines.length){var mid=innerHeight*0.55,best=-1,bd=1e9;
    stackLines.forEach(function(p,i){var r=p.getBoundingClientRect(),c=(r.top+r.bottom)/2,d=Math.abs(c-mid);if(c<mid+40&&d<bd){bd=d;best=i}});
    stackLines.forEach(function(p,i){p.classList.toggle('now',i===best);p.classList.toggle('past',best>=0&&i<best)})}
  if(!REDUCE)ghosts.forEach(function(g){var r=g.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;
    var k=(r.top+r.height/2-innerHeight/2)/innerHeight;g.style.translate='0 '+(k*60).toFixed(1)+'px'});
}

/* ---------- thanh trên cùng: tên phần đang đọc, số thứ tự, tiến độ ---------- */
var ttl=document.getElementById('mttl'),cnt=document.getElementById('mcnt'),bar=document.getElementById('mbar'),list=document.getElementById('mlist'),btn=document.getElementById('mtoc'),cur=-1,ticking=false;
function onScroll(){ticking=false;var y=innerHeight*0.35,idx=0;
  for(var i=0;i<N;i++){if(secs[i].getBoundingClientRect().top<=y)idx=i;else break}
  if(idx!==cur){cur=idx;ttl.textContent=secs[idx].dataset.title||'';cnt.textContent=pad(idx+1)+' / '+pad(N);
    if(!REDUCE){ttl.classList.remove('swap');void ttl.offsetWidth;ttl.classList.add('swap')}
    $$('a',list).forEach(function(a,n){a.classList.toggle('cur',n===idx)})}
  var h=document.documentElement.scrollHeight-innerHeight;bar.style.width=(h>0?Math.min(100,Math.max(0,scrollY/h*100)):0)+'%';
  scrollFx();
}
addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
addEventListener('resize',onScroll);

/* ---------- mục lục ---------- */
list.innerHTML=secs.map(function(s,i){return '<a href="#s'+(i+1)+'"><em>'+pad(i+1)+'</em><span>'+esc(s.dataset.title)+'</span></a>'}).join('');
btn.addEventListener('click',function(){list.hidden=!list.hidden;btn.setAttribute('aria-expanded',String(!list.hidden))});
list.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;e.preventDefault();list.hidden=true;btn.setAttribute('aria-expanded','false');
  document.getElementById(a.getAttribute('href').slice(1)).scrollIntoView({behavior:REDUCE?'auto':'smooth',block:'start'})});
onScroll();
window.__mobile={state:function(){return {cur:cur+1,total:N,shown:$$('#stage .mr.mr-in').length,steps:targets.length,pending:$$('#stage .mr.mr-pending').length}}};
})();
