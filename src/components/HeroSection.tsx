import { Button } from "@chakra-ui/react";
import styles from "../styles/HeroSection.module.css";

const HeroSection = () => {
  return (
    <div className={styles.parent}>
      {" "}
      <div className={styles.card}>
        <h1 className={styles.header}>
          {" "}
          <span>Escape to paradise</span>
        </h1>
        <p>Discover the beauty of a Tropical Island Getaway</p>

        <div className={styles.buttons}>
          <Button variant={"solid"} colorScheme="telegram">
            Learn more
          </Button>

          <Button variant={"solid"} colorScheme="yellow">
            Book now
          </Button>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
