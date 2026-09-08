from pathlib import Path

p = Path('lab/capsules-approfondies.html')
s = p.read_text(encoding='utf-8')

if '.box.videobox{' not in s:
    css = '''
.box.videobox{grid-column:1/-1;border-left:6px solid #6b3fa0;background:#faf7ff}.video-wrap{display:grid;grid-template-columns:minmax(280px,1.2fr) minmax(220px,.8fr);gap:14px;align-items:center}.video-frame{position:relative;width:100%;padding-top:56.25%;background:#11151b;border-radius:12px;overflow:hidden}.video-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.video-info b{display:block;font-size:16px;margin-bottom:5px}.video-info span{display:block;color:var(--muted);font-size:13px;margin-bottom:10px}.video-info a{display:inline-block;background:#11151b;color:#fff;text-decoration:none;border-radius:9px;padding:9px 12px;font-weight:800}.video-note{font-size:12px;color:var(--muted);margin-top:9px}@media(max-width:700px){.video-wrap{grid-template-columns:1fr}}
'''
    s = s.replace('</style></head>', css + '</style></head>', 1)

if 'const videosFR={' not in s:
    js = r'''const videosFR={
  virtu:{id:'CJyYlTevyOA',title:'La virtualisation expliquée : hyperviseur type 1 et type 2',channel:'DanyTech'},
  virtualbox:{id:'SUVZg4hlvpI',title:'Installer, configurer et créer une machine virtuelle avec VirtualBox',channel:'Jojojuju9'},
  vbnet:{id:'iPPKNc3appk',title:'VirtualBox Networking : NAT, Bridge, Host-Only, réseau interne…',channel:'IT-Connect - Florian'},
  vmware:{id:'KCeX-65ohRA',title:'Débuter avec VMware Workstation Pro : créer une VM',channel:'IT-Connect - Florian'},
  vmwarenet:{id:'hj-deoZA4do',title:'VMware Workstation Pro : NAT, Bridged, Host-only et LAN Segment',channel:'IT-Connect - Florian'},
  vmwaresnap:{id:'4OY057KMe6M',title:'VMware Workstation Pro : les snapshots',channel:'IT-Connect - Florian'},
  docker:{id:'uqHG3VaGybU',title:'Docker pour débutants : images, conteneurs, Docker Hub, volumes et Nginx',channel:'PlaisirArduino'},
  dockerfile:{id:'Aa-_cJtqEVs',title:'Dockerfile, premier conteneur et Docker Hub',channel:'SFYNX TUTORIEL Français'},
  compose:{id:'N6-btSWwFDg',title:'Docker Compose : comprendre et déployer plusieurs services',channel:'La Minute Agile'},
  portainer:{id:'TSfUY3qJv88',title:'Docker, Docker Compose et Portainer avec une interface graphique',channel:'GuiPoM - G. testé !'},
  kuma:{id:'RtRnHzL-LoA',title:'Uptime Kuma : superviser facilement ses services',channel:'IT-Connect - Florian'},
  proxmox:{id:'NKJ-giXCyuU',title:'Installer Proxmox VE pas à pas : guide complet pour débuter',channel:'Superzoulouworld'},
  proxmoxTemplate:{id:'xfOKS853aXI',title:'Proxmox : créer un template de VM et préparer Cloud-init',channel:'The Duke of Puteaux'},
  ad:{id:'0MoFlwpylHM',title:'Installation et configuration Active Directory + DNS sur Windows Server',channel:'Objectif Learning'},
  adgroup:{id:'zukkRs6xA7o',title:'Créer et gérer un groupe d’utilisateurs dans Active Directory',channel:'MOG ACADEMY'},
  gpo:{id:'9hN5xqkGCG0',title:'Windows Server : créer une stratégie de groupe GPO',channel:'LinkedIn Learning français'},
  cloud:{id:'I0R9RTLOOXw',title:'Le cloud expliqué en français : AWS, Azure, GCP, EC2 et VPC',channel:'cocadmin'}
};
function videoFor(m){
  const exact={
    S01:'virtu',S02:'virtu',S03:'virtu',S04:'virtualbox',S05:'vmwaresnap',S06:'virtu',
    H01:'virtu',H02:'virtualbox',H03:'virtualbox',H04:'vmwaresnap',H05:'virtualbox',H06:'virtualbox',
    W01:'vmware',W02:'vmware',W03:'vmwarenet',W04:'vmwaresnap',W05:'vmware',W06:'vmware',
    D01:'docker',D02:'docker',D03:'docker',D04:'dockerfile',D05:'docker',D06:'docker',D07:'docker',D08:'docker',D09:'compose',D10:'docker',D11:'docker',D12:'compose',D13:'portainer',D14:'kuma',D15:'portainer',
    P01:'proxmox',P02:'proxmox',P03:'proxmox',P04:'proxmox',P05:'proxmox',P06:'proxmoxTemplate',P07:'proxmox',P08:'proxmox',P09:'proxmox',
    N01:'vbnet',N02:'vbnet',N03:'vbnet',N04:'vbnet',N05:'vbnet',N06:'vbnet',
    A01:'ad',A02:'ad',A03:'adgroup',A04:'ad',A05:'gpo',A06:'ad',
    C01:'cloud',C02:'cloud',C03:'cloud',C04:'cloud',C05:'cloud',
    PED01:'virtu',PED02:'virtu',PED03:'virtu',PED04:'virtu'
  };
  return videosFR[exact[m.id] || 'virtu'];
}
function videoBox(m){
  const v=videoFor(m);
  const url='https://www.youtube.com/watch?v='+v.id;
  const embed='https://www.youtube-nocookie.com/embed/'+v.id;
  return `<section class="box videobox"><h4>Vidéo en français · avant la manipulation</h4><div class="video-wrap"><div class="video-frame"><iframe loading="lazy" src="${embed}" title="${v.title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><div class="video-info"><b>${v.title}</b><span>${v.channel}</span><a href="${url}" target="_blank" rel="noreferrer">Ouvrir la vidéo sur YouTube</a><div class="video-note">Vidéo sélectionnée en français pour introduire ou illustrer la notion de cette capsule. Elle complète le contenu technique et le mini-lab.</div></div></div></section>`;
}
'''
    s = s.replace('function list(arr){', js + '\nfunction list(arr){', 1)

if '${videoBox(m)}' not in s:
    old = '<section class="box securitybox"><h4>Critères de sécurité</h4>${list(m.sec)}</section><section class="box practice">'
    new = '<section class="box securitybox"><h4>Critères de sécurité</h4>${list(m.sec)}</section>${videoBox(m)}<section class="box practice">'
    if old not in s:
        raise SystemExit('Zone openModule introuvable')
    s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
