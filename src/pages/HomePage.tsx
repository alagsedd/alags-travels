import HeroSection from "../components/HeroSection";
import PopularTours from "../components/PopularTours";
import Slider from "../components/Slider";
import styles from "../styles/HomePage.module.css";

const HomePage = () => {
  return (
    <div className={styles.parent}>
      <Slider />
      <HeroSection />
      <PopularTours />
    </div>
  );
};

export default HomePage;
