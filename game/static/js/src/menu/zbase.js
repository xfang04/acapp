class AcGameMenu{
    constructor(root) {
        this.root = root;
        this.$menu = $(`
        <div class="ac-game-menus"</div>
        `);
        this.root.$ac_game.append(this.$menu);
    }
}
