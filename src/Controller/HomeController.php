<?php

namespace App\Controller;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\Persistence\ManagerRegistry;
use App\Entity\Game;

#[Route('/')]
class HomeController extends AbstractController
{
    #[Route(['/', '/home'])]
    public function index(ManagerRegistry $doctrine): Response
    {
        return $this->render('home.html.twig');
    }
}