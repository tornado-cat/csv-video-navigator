(async function () {
  const player = document.getElementById("player");
  const titleEl = document.getElementById("title");

  const res = await fetch("/api/videos");
  const files = await res.json(); 

  let idx = 0;

  if (!files || files.length === 0) {
    alert("videos.csv içerisinde hiç URL bulunamadı (en azından 'url' kolonu gerek).");
    return;
  }

  function setTitle(text) {
    titleEl.textContent = text || "";
    titleEl.style.display = text ? "block" : "none";
  }

  function load(i) {
    idx = (i + files.length) % files.length;
    const current = files[idx];
    player.src = current.url;       
    player.removeAttribute("controls"); // oyalttaki barı kaldırma
    setTitle(current.title);
    player.pause(); 
  }

  load(0);

  // Klavye kısayolları
  document.addEventListener("keydown", (e) => {
    const tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea" || e.target.isContentEditable) return;

    if (e.key === "a" || e.key === "A") {
      load(idx - 1);
    } else if (e.key === "d" || e.key === "D") {
      load(idx + 1);
    } else if (e.key === " ") {
      e.preventDefault();
      if (player.paused) player.play();
      else player.pause();
    }
  });

  // Videoya tıklayınca oynat/durdur
  player.addEventListener("click", () => {
    if (player.paused) player.play();
    else player.pause();
  });

  // Bittiğinde otomatik sonraki
  player.addEventListener("ended", () => load(idx + 1));
})();
