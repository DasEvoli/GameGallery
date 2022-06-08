<?php

namespace App\Controller;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\Persistence\ManagerRegistry;
use Symfony\Component\HttpFoundation\JsonResponse;

#[Route('/api/gamelist')]
class GamesController extends AbstractController
{
    #[Route('/challenges')]
    public function index(ManagerRegistry $doctrine): Response
    {
        $records = $doctrine->getRepository("App\Entity\Game")->findAll();
        
        $json_arr = [];

        foreach($records as $record){
            
            $id = $record->getId();
            $console_name = $record->getConsoleName();
            $game_name = $record->getGameName();
            $collection_name = $record->getCollectionName();
            $genre = $record->getGenre();
            $time = $record->getTime();
            $score = $record->getScore();
            $video_url = $record->getVideoUrl();
            $speedrun = $record->isSpeedrun();
            $cover = $record->getCover();

            $obj =  [
                        'id' => $id,
                        'console_name' => $console_name,
                        'game_name' => $game_name,
                        'collection_name' => $collection_name,
                        'genre' => $genre,
                        'time' => $time,
                        'score' => $score,
                        'video_url' => $video_url,
                        'speedrun' => $speedrun,
                        'cover' => $cover
                    ];

            array_push($json_arr, $obj);
        }

        return new JsonResponse(json_encode($json_arr));
    }

    #[Route('/upcoming')]
    public function upcoming(ManagerRegistry $doctrine): Response
    {
        $json_arr = [];

        $records = $doctrine->getRepository("App\Entity\Upcoming")->findAll();
        foreach($records as $record){
            
            $id = $record->getId();
            $game_name = $record->getGameName();
            $cover = $record->getCover();
            $obj =  [
                'id' => $id,
                'game_name' => $game_name,
                'cover' => $cover
            ];
            array_push($json_arr, $obj);
        }

        return new JsonResponse(json_encode($json_arr));
    }
}