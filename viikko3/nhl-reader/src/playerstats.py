

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        stats = []
        players = [player for player in self.reader.get_players() if player.nationality == nationality]
        for player in sorted(players, key=lambda player: player.total, reverse=True):
            stats.append(player.__str__())

        return stats