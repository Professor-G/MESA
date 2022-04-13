program run
use run_star_support, only: do_read_star_job
use run_star, only: do_run_star

implicit none

integer :: ierr, n_mods
character (len=32) :: inlist_fname, mass_formatted, mass_list
logical :: test_log
real :: mass
integer :: i

ierr = 0

open(2, file="mass_list.txt", status = "old")
read(2, *) n_mods
do i=1, n_mods
    read(2, *)  mass_formatted
    ! mass = 0.3 + 1.313333 * (i - 1)
    ! mass_formatted = "brew install gfortran"
    ! write(mass_formatted, '(F 0 5.02)') mass
    ! if (mass_formatted(1:1) == " ") then
        ! mass_formatted(1:1) = "0"
    ! else
    ! end if
    inlist_fname = "inlist_"//mass_formatted

    print *, inlist_fname
    call do_read_star_job(inlist_fname, ierr)
    if (ierr == 0) then
        call do_run_star(inlist_fname)
    end if
end do

end program
