import React, { ReactNode } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../Navbar/Navbar.module.scss";
import logo from "../../assets/icons/lectarium-logo.svg";
import help from "../../assets/icons/help.svg";
import main from "../../assets/icons/main.svg";
import glossary from '../../assets/icons/glossary.svg'
import profile from "../../assets/icons/profile.svg";

type Props = {
  children?: ReactNode;
};

export const Navbar: React.FC<Props> = ({ children }) => {
  const navigate = useNavigate();
  return (
    <div className={styles.navbar}>
      <div className={styles.wrapper}>
        <div className={styles.logo}>
          <img src={logo} alt="" />
        </div>
        <div className={styles.menu}>
          <button
            className={styles.btn}
            onClick={() => {
              navigate("/main");
            }}
          >
            <img className={styles.icon} src={main} alt="" />
            Главная
          </button>
          <button
            className={styles.btn}
            onClick={() => {
              navigate("/help");
            }}
          >
            <img className={styles.icon} src={help} alt="" />
            Помощь
          </button>
          <button
            className={styles.btn}
            onClick={() => {
              navigate("/archive");
            }}
          >
            <img className={styles.icon} src={profile} alt="" />
            Архив
          </button>
          <button
            className={styles.btn}
            onClick={() => {
              navigate("/glossary");
            }}
          >
            <img className={styles.icon} src={glossary} alt="" />
            Глоссарий
          </button>
        </div>
      </div>
      <div className="pt-12 pr-16 w-full">
      {children}
      </div>
      
    </div>
  );
};
