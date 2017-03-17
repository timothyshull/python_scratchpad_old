use strict;
use warnings;

my $fmap = $fmap_array->[$idx];

my $ssd;
my $hdd;

if ($fmap->{'type'} =~ m#ssd#)
{
    next if ($fmap->{'marked'});
    $ssd = $ssds[0];

    if ($fmap->{'type'} =~ m#:#)
    {
        _fill_ahead($fmap_array, $idx, $ssd, 'ssd');
    }
    else
    {
        %$fmap = (%$ssd, %$fmap);
    }
    shift(@ssds);
}
