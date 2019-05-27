var currentPick = 1;

new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        players: [],
        teams: [],
        currentTeam: undefined,
        currentSelectedPlayer: undefined,
    }
});

Vue.component('player', {
    props: ['info'],
    data: function() {
        return {
            drafted: false
        }
    },
    template: `
        <tr>
            <td class="draftRank">[[info.rank]]</td>
            <td class="playerName">[[info.name]]</td>
            <td class="playerTeam">[[info.team]]</td>
            <td class="playerPosition">[[info.position]]</td>
            <td class="bye">[[info.bye]]</td>
            <td class="points">[[info.points]]</td>
            <td>[[info.num_catches]]</td>
            <td>[[info.receiving_yards]]</td>
            <td>[[info.num_rushes]]</td>
            <td>[[info.rushing_yards]]</td>
            <td>[[info.num_passes]]</td>
            <td>[[info.passing_yards]]</td>
        </tr>
    `,
});

Vue.component('picked-player', {
    props: ['info'],
    template: `
        <tr>
            <td class=pickedPosition>[[info.position]]</td>
            <td class="playerName">[[info.name]]</td>
        </tr>
    `,
});

Vue.component('current-team-player', {
    props: ['info'],
    template: `
        <tr>
            <td>[[info.position]]</td>
            <td>[[info.name]]</td>
            <td>[[info.bye]]</td>
        </tr>
    `
});

Vue.component('current-selected-player', {
    props: ['info'],
    template: `
        <div>
            <img src=[[info.pic]] alt="Image of selected player">
            <h4>[[info.name]], [[info.team]] [[info.position]]</h4>
            <p>Bye: [[info.bye]]</p>
            <button v-bind:class="{ inactive: info.drafted}">Draft Player</button>
        </div>
    `
});


