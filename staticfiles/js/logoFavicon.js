const urlHolder = document.querySelector("#url-holder");

function setLogo() {
    const logo = document.querySelector("img.logo");
    logo.setAttribute("src", urlHolder.getAttribute("logo-url"));
}

function setFavicon() {
    const link = document.querySelector("link[rel~='icon']");
    if (!link) {
        link = document.createElement('link');
        link.rel = 'icon';
        document.head.appendChild(link);
    }
    link.href = urlHolder.getAttribute("favicon-url");
}

setLogo();
setFavicon();