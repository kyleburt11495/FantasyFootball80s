new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        players: [],
        teams: [],
    }
});

Vue.component('player', {
    props: ['info'],
    template: `
        <tr>
            <td class="draftRank">[[info.rank]]</td>
            <td class="playerName">[[info.name]]</td>
            <td class="bye">[[info.bye]]</td>
            <td class="points">[[info.points]]</td>
        </tr>
    `
});


