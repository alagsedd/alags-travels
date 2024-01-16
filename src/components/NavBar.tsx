import { useState } from "react";
import styles from "../styles/NavBar.module.css";
import { IoMenuSharp } from "react-icons/io5";
import { IoClose } from "react-icons/io5";
import { Link } from "react-router-dom";

const NavBar = () => {
  const [showMenu, setShowMenu] = useState(false);

  return (
    <>
      <nav className={styles.nav}>
        <div className={styles.brandName}>
          <span>A-Travels</span>
        </div>

        {showMenu ? (
          <IoClose
            className={styles.toggleTool}
            onClick={() => setShowMenu(false)}
            size="30"
          />
        ) : (
          <IoMenuSharp
            className={styles.toggleTool}
            onClick={() => setShowMenu(true)}
            size="30"
          />
        )}
      </nav>

      {showMenu && (
        <ul className={styles.verticalNav}>
          <li>
            <Link className={styles.link} to={"/"}>
              Home
            </Link>
          </li>

          <li>
            <Link className={styles.link} to={"#"}>
              Destinations
            </Link>
          </li>

          <li>
            <Link className={styles.link} to={"#"}>
              About us
            </Link>
          </li>

          <li>
            <Link className={styles.link} to={"#"}>
              Special Offers
            </Link>
          </li>
        </ul>
      )}
    </>
  );
};

export default NavBar;
