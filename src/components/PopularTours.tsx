import styles from "../styles/PopularTours.module.css";
import tower from "../assets/images/effiel-tower.jpg";
import mountain from "../assets/images/mountain.jpg";
import p3 from "../assets/images/colosseum.jpg";
import TourCard from "../cards/TourCard";

const PopularTours = () => {
  const tours = [
    { id: 1, name: "Effiel Tower", image: tower },
    { id: 2, name: "Death Valley", image: mountain },
    { id: 3, name: "Colosseum", image: p3 },
    { id: 4, name: "Death Valley", image: p3 },
    { id: 5, name: "Death Valley", image: mountain },
  ];

  return (
    <>
      <div className={styles.parent}>
        <h2 className={styles.header}>
          <span>Popular Tours</span>
        </h2>

        <div className={styles.imgContainer}>
          {tours.map((item) => (
            <TourCard image={item.image} name={item.name} key={item.id} />
          ))}
        </div>
      </div>
    </>
  );
};

export default PopularTours;
