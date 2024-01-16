import styles from "../styles/Slider.module.css";
// import Swiper core and required modules
import {
  Navigation,
  Pagination,
  Scrollbar,
  A11y,
  Autoplay,
} from "swiper/modules";

import { Swiper, SwiperSlide } from "swiper/react";

// Import Swiper styles
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/autoplay";
import "swiper/css/pagination";
import "swiper/css/scrollbar";
import s1 from "../assets/images/slider3.jpg";
import s2 from "../assets/images/slider2.jpg";
import s3 from "../assets/images/slider4.jpg";
import s4 from "../assets/images/slider5.jpg";

const Slider = () => {
  const sliders = [s2, s1, s3, s4];

  return (
    <>
      <div className={styles.parent}>
        {" "}
        <Swiper
          className={styles.swiper}
          // install Swiper modules
          modules={[Navigation, Autoplay, Pagination, Scrollbar, A11y]}
          spaceBetween={0}
          autoplay={{
            delay: 4000,
          }}
          slidesPerView={1}
          pagination={{ clickable: true }}
          scrollbar={{ draggable: true }}
        >
          {sliders.map((item, index) => (
            <SwiperSlide key={index}>
              {" "}
              <img
                className={styles.image}
                src={item}
                alt="Your browser doesn't support this image"
              />
            </SwiperSlide>
          ))}
        </Swiper>
      </div>
    </>
  );
};

export default Slider;
