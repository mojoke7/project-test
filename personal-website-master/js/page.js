const Modals = function() {
    this.projectModal = document.querySelector('#projectModal');
    this.aboutModal = document.querySelector('#aboutModal');
    this.contactModal = document.querySelector('#contactModal');
    this.background = document.querySelector("#modal");
    this.closeProject = document.querySelector("#closeProject");
    this.closeAbout = document.querySelector("#closeAbout");
}

Modals.prototype.showAboutModal = function() {
    this.background.style.display = "block";
    this.aboutModal.style.display = "grid";
}


Modals.prototype.showProjectModal = function() {
    this.background.style.display = "block";
    this.projectModal.style.display = "block";
}

Modals.prototype.showContactModal = function() {
    this.background.style.display = "block";
    this.contactModal.style.display = "block";
}


Modals.prototype.reset = function() {
    this.background.style.display = "none";
    this.aboutModal.style.display = "none";
    this.projectModal.style.display = "none";
    this.contactModal.style.display = "none";
}

const modal = new Modals();

document.addEventListener('click', function(e) {
    switch (e.target.id) {
        case "aboutBtn":
            modal.showAboutModal();
            break;
        case "projectBtn":
            modal.showProjectModal();
            break;
        case "contactBtn":
            modal.showContactModal();
            break;
        case "modal":
            modal.reset();
            break;
        case "closeProject":
            modal.reset();
            break;
        case "closeAbout":
            modal.reset();
            break;
        case "closeContact":
            modal.reset();
            break;
    };
});