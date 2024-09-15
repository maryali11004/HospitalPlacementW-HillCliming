import random


class Space:
    def __init__(self, height, width, num_hospitals):
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set()
        self.hospitals = set()

    def add_house(self, row, col):
        self.houses.add((row, col))

    def available_space(self):
        candidates = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)  # Fixed typo
        )
        for house in self.houses:
            candidates.remove(house)
        for hospital in self.hospitals:  # Fixed typo
            candidates.remove(hospital)
        return candidates

    def get_cost(self, hospitals):
        cost = 0
        for house in self.houses:
            cost += min(
                abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
                for hospital in hospitals
            )  # the absolute difference in the x axis + in the y
        return cost

    def get_neighbors(self, row, col):  # Fixed no return
        candidates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        neighbors = []
        for r, c in candidates:
            if (r, c) in self.houses or (r, c) in self.hospitals:
                continue
            if 0 <= r < self.height and 0 <= c < self.width:
                neighbors.append((r, c))
        return neighbors  # Added return

    def output_image(self, filename):
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size + cost_size + padding * 2),
            "white"
        )
        house = Image.open("/Users/maryamabdelfattah/Downloads/PRJECTS/HillClimbing/assets/House.jpg").resize((cell_size, cell_size))
        hospital = Image.open("/Users/maryamabdelfattah/Downloads/PRJECTS/HillClimbing/assets/Hospital.jpg").resize((cell_size, cell_size))
        font = ImageFont.truetype("/Users/maryamabdelfattah/Downloads/PRJECTS/HillClimbing/assets/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):
                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="black")
                if (i, j) in self.houses:
                    img.paste(house, rect[0])  # Fixed extra argument
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0])  # Fixed extra argument

        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "black"
        )

        draw.text(
            (padding, self.height * cell_size + padding),
            f"cost: {self.get_cost(self.hospitals)}",  # Fixed typo
            fill="white",
            font=font
        )
        img.save(filename)

    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        count = 0
        self.hospitals = set()
        for i in range(self.num_hospitals):
            self.hospitals.add(random.choice(list(self.available_space())))

        if log:
            print("initial state: cost", self.get_cost(self.hospitals))
        if image_prefix:
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

        while maximum is None or count < maximum:
            count += 1
            best_neighbors = []
            best_neighbor_cost = None

            for hospital in self.hospitals:
                for replacement in self.get_neighbors(*hospital):  # Fixed typo
                    neighbor = self.hospitals.copy()  # Fixed typo
                    neighbor.remove(hospital)
                    neighbor.add(replacement)

                    cost = self.get_cost(neighbor)
                    if best_neighbor_cost is None or cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]  # Fixed assignment
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            if best_neighbor_cost >= self.get_cost(self.hospitals):
                return self.hospitals
            else:
                if log:
                    print(f"better neighbor: cost {best_neighbor_cost}")
                self.hospitals = random.choice(best_neighbors)
            if image_prefix:
                self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")


s = Space(height=6, width=12, num_hospitals=2)
for i in range(5):
    s.add_house(random.randrange(s.height), random.randrange(s.width))

hospitals = s.hill_climb(image_prefix="hospitals", log=True)
