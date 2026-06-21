function chartLine(id, labels, data){
  const el=document.getElementById(id); if(!el) return;
  new Chart(el,{type:'line',data:{labels,datasets:[{data,tension:.38,fill:true,borderWidth:3,pointRadius:4}]},options:{responsive:true,plugins:{legend:{display:false}},scales:{x:{grid:{color:'rgba(255,255,255,.05)'},ticks:{color:'#9da0aa'}},y:{grid:{color:'rgba(255,255,255,.06)'},ticks:{color:'#9da0aa'}}}}});
}
function chartDoughnut(id){
  const el=document.getElementById(id); if(!el) return;
  new Chart(el,{type:'doughnut',data:{labels:['Recebido','Pendente'],datasets:[{data:[85,15],borderWidth:0}]},options:{plugins:{legend:{position:'bottom',labels:{color:'#f7f7f8'}}},cutout:'72%'}});
}
function toastDemo(titulo){Swal.fire({title:titulo,text:'Ação demonstrativa executada com sucesso.',icon:'success',background:'#111216',color:'#fff',confirmButtonColor:'#ef1f25'});}
window.addEventListener('load',()=>{
 chartLine('alunosChart',['01','05','10','15','20','25','30'],[24,39,58,72,91,108,128]);
 chartDoughnut('receitaChart');
 chartLine('pesoChart',['15/04','15/05','15/06','15/07'],[67.5,66.2,65.1,64.8]);
 chartLine('mobilePesoChart',['S','T','Q','Q','S','S','D'],[68,67,67.5,66.8,66.2,65.8,66.4]);
 chartLine('evolucaoFullChart',['15/04','15/05','15/06','15/07'],[67.5,66.2,65.1,64.8]);
});
