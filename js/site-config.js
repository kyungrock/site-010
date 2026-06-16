/** Azure Static Web Apps 배포 URL (로컬·다른 호스트는 자동 보정) */
window.SITE_CONFIG = {
  baseUrl: "https://site-010.azurestaticapps.net",
  siteName: "전 샤워",
  slug: "site-010",
  defaultDescription:
    "마사지 전 샤워, 청결·혈행 케어 가이드. 힐링·웰니스·셀프케어를 위한 실용 정보 허브.",
  locale: "ko_KR",
  keywords: "마사지전샤워,마사지,힐링,웰니스,셀프케어",
};

function getSiteBase() {
  const cfg = window.SITE_CONFIG?.baseUrl;
  if (cfg && !location.hostname.includes("localhost") && !location.protocol.startsWith("file")) {
    return cfg.replace(/\/$/, "");
  }
  const path = location.pathname.replace(/\/[^/]*$/, "");
  return (location.origin + path).replace(/\/$/, "") || location.origin;
}

function absoluteUrl(relativePath) {
  const base = getSiteBase();
  const path = String(relativePath || "")
    .replace(/^\//, "")
    .replace(/^https?:\/\//, "");
  if (path.startsWith("http")) return path;
  return `${base}/${path}`;
}
