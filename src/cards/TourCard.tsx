import { useState } from "react";
import styles from "../styles/TourCard.module.css";
import { FaHeart } from "react-icons/fa";

interface Props {
  image: string;
  name: string;
}

const TourCard = ({ image, name }: Props) => {
  const [clicked, setClicked] = useState(false);

  return (
    <div className={styles.card}>
      <img
        className={styles.image}
        src={image}
        alt="Your browser doesn't support this image"
      />

      <div className={styles.sub}>
        <span>{name}</span>
        <FaHeart
          className={styles.icon}
          size={"23"}
          onClick={() => setClicked(!clicked)}
          color={clicked ? "red" : "#fff"}
        />
      </div>
    </div>
  );
};

export default TourCard;
