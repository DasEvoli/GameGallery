<?php

namespace App\Entity;

use App\Repository\GameRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: GameRepository::class)]
class Game
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column(type: 'integer')]
    private $id;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $console_name;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $game_name;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $collection_name;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $genre;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $time;

    #[ORM\Column(type: 'integer', nullable: true)]
    private $score;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $video_url;

    #[ORM\Column(type: 'boolean', nullable: true)]
    private $speedrun;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getConsoleName(): ?string
    {
        return $this->console_name;
    }

    public function setConsoleName(string $console_name): self
    {
        $this->console_name = $console_name;

        return $this;
    }

    public function getGameName(): ?string
    {
        return $this->game_name;
    }

    public function setGameName(?string $game_name): self
    {
        $this->game_name = $game_name;

        return $this;
    }

    public function getCollectionName(): ?string
    {
        return $this->collection_name;
    }

    public function setCollectionName(?string $collection_name): self
    {
        $this->collection_name = $collection_name;

        return $this;
    }

    public function getGenre(): ?string
    {
        return $this->genre;
    }

    public function setGenre(?string $genre): self
    {
        $this->genre = $genre;

        return $this;
    }

    public function getTime(): ?string
    {
        return $this->time;
    }

    public function setTime(?string $time): self
    {
        $this->time = $time;

        return $this;
    }

    public function getScore(): ?int
    {
        return $this->score;
    }

    public function setScore(?int $score): self
    {
        $this->score = $score;

        return $this;
    }

    public function getVideoUrl(): ?string
    {
        return $this->video_url;
    }

    public function setVideoUrl(?string $video_url): self
    {
        $this->video_url = $video_url;

        return $this;
    }

    public function isSpeedrun(): ?bool
    {
        return $this->speedrun;
    }

    public function setSpeedrun(?bool $speedrun): self
    {
        $this->speedrun = $speedrun;

        return $this;
    }
}
