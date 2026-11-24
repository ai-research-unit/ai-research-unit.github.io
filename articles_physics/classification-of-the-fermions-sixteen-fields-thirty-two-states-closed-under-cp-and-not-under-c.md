# __Classification of the Fermions: One Generation, Sixteen Fields, Thirty-Two States, Closed Under $CP$ and Not Under $C$__

## Introduction

**The question.** The bosons fill the cells of the three grids. Do the fermions fill them too, how many are there, and what happens to a fermion under charge conjugation?

**The answer.**

$$
\underbrace{4}_{\text{quartet}}\times\underbrace{2}_{\text{doublet slot}}\times\underbrace{2}_{\text{chirality block}}=16\ \text{per generation},
\qquad
C:\ (\mathbf4,\mathbf2,\mathbf1)\mapsto(\bar{\mathbf4},\mathbf2,\mathbf1),
$$

with the sixteen already containing their own antiparticles as conjugate modes, thirty-two states per generation, and the spectrum closed under $CP$ with $L\leftrightarrow R$ and not under $C$.

**What this article is.** The fermion side of the classification, and its conjugation. It states the product that counts a generation, why the product is the right operation here and the sum of squares is not, then writes the sixteen as two octets, one per chirality block, names the rows, and conjugates them: the operation, the antiparticle charges, the count of fields against the count of states, and what the map fails to do. The group, its three numbers, the ledger and the cells the bosons occupy are [Classification of the Bosons](classification-of-the-bosons-twenty-four-cells-twenty-one-generators-one-name-in-every-cell.html).

**Where the sixteen sits on the picture.** A fermion occupies one quartet index and one doublet index, so a row is a pair of labels and not a cell of the $4\times4$. The $4$ is the quartet's size, the $2$ is a doublet's size, and the second $2$ is the chirality block — which $2\times2$ grid the doublet index belongs to. **The grids are shared with the bosons; the reading is not**: a boson is a direction inside one factor, a fermion is a product of one value from each.

**What this article is not.** It is not a flavour article, and it says nothing about why there are three generations. The number of generations is not fixed by the grid; that is the subject of [The Excitation Ladder Theory of Flavour](the-excitation-ladder-theory-of-flavour.html) and its companions. Nor is it a mass article: the masses of these states come from the Yukawa sector, which the frame does not fix.

## The Count Is a Product, Not a Sum of Squares

**The fermions are a product, because a fermion carries one value of every index.** One quartet value, one doublet slot, and one chirality. The count is therefore

$$
\underbrace{4}_{\text{quartet}}\times\underbrace{2}_{\text{doublet slot}}\times\underbrace{2}_{\text{chirality block}}=16 ,
$$

and **$16$ is literally the product of the model's three numbers.** That is the answer to "why sixteen": it is $4\times2\times2$, and each factor contributes the size of its own index.

**The product is taken block by block, and that is where the count has to be done carefully.** The sixteen is not one block of $4\times2\times2$ components; it is two blocks, and in each block one factor is a singlet:

$$
(\mathbf4,\mathbf2,\mathbf1):\ 4\times2\times1=8
\qquad
(\bar{\mathbf4},\mathbf1,\mathbf2):\ 4\times1\times2=8
\qquad
8+8=16 .
$$

The sum of the two blocks equals the full product because $1+1=2$:

$$
4\times2\times1+4\times1\times2=4\times2\times(1+1)=4\times2\times2=16 .
$$

**So the identity $16=4\times2\times2$ holds, and it holds by distributing over the two blocks, not by any single representation having sixteen components in the shape $4\otimes2\otimes2$.** The difference is not pedantry: in $(\mathbf4,\mathbf2,\mathbf2)$ both weak factors act on the same field, while in the actual spectrum a left-handed field is a doublet of $\mathrm{SU}(2)_L$ and a **singlet** of $\mathrm{SU}(2)_R$.

| the job | the operation on $4,2,2$ | the arithmetic | the result |
|---|---|---|---|
| the boson cells | sum of squares | $4^2+2^2+2^2$ | $24$ |
| the boson generators | each square minus one | $15+3+3$ | $21$ |
| the fermions, left block | product with the third factor trivial | $4\times2\times1$ | $8$ |
| the fermions, right block | product with the second factor trivial | $4\times1\times2$ | $8$ |
| the fermions, both blocks | the two added | $8+8$ | $16$ |
| the full product | distributing $1+1=2$ | $4\times2\times2$ | $16$ |

**Two of the three numbers are $2$, they are not the same $2$.** One is a doublet's size, the other is the chirality block, and they never multiply inside one field, because no fermion is a doublet of both weak groups at once.

**The one genuine coincidence, stated as one.** The number $16$ is also the dimension of the bifundamental $(\mathbf4,\mathbf2,\mathbf2)$, because $4\times2\times2$ does not care which factor is which. **The fermion content of this model is not that representation**; the equality is arithmetic, and the block table above is what distinguishes the two objects.

## The Fermions, on the Same Cells

**Sixteen per generation, and they occupy the cells of the $4\times4$ grid times the cells of the two $2\times2$ grids.** A fermion is one quartet index (four values) times one doublet index (two values per chirality), and $4\cdot2=8$ per chirality, so $16$ per generation. **That is the product rule of §*The Count Is a Product, Not a Sum of Squares*, read off the grids.** The tables below are the rule written out, one row per value of each index.

**The left octet: the $4\times4$ index times the $L$ grid's up/down.**

| fermion | quartet index | $L$ index | $Q$ | $B-L$ |
|---|---|---|---|---|
| $\xi_{\mathrm{neu},eL}$ | $t$ | $\uparrow$ | $0$ | $-1$ |
| $e_{L}$ | $t$ | $\downarrow$ | $-1$ | $-1$ |
| $u^{r}_{L}$ | $r$ | $\uparrow$ | $+\tfrac23$ | $+\tfrac13$ |
| $d^{r}_{L}$ | $r$ | $\downarrow$ | $-\tfrac13$ | $+\tfrac13$ |
| $u^{g}_{L}$ | $g$ | $\uparrow$ | $+\tfrac23$ | $+\tfrac13$ |
| $d^{g}_{L}$ | $g$ | $\downarrow$ | $-\tfrac13$ | $+\tfrac13$ |
| $u^{b}_{L}$ | $b$ | $\uparrow$ | $+\tfrac23$ | $+\tfrac13$ |
| $d^{b}_{L}$ | $b$ | $\downarrow$ | $-\tfrac13$ | $+\tfrac13$ |

**The right octet: the same four indices times the $R$ grid.** $\xi_{\mathrm{neu},eR}$, $e_R$, $u^{r}_{R}$, $d^{r}_{R}$, $u^{g}_{R}$, $d^{g}_{R}$, $u^{b}_{R}$, $d^{b}_{R}$, with $Q$ and $B-L$ identical to the left octet's rows. What differs is which $2\times2$ grid the doublet index belongs to.

**Three remarks about the pairing.**

- **The colour index is $\mathbf3$ on the left and $\bar{\mathbf3}$ on the right, and the two readings differ in the sign of $Q$.** The four labels are the same four, but the right octet sits in the conjugate quartet, which is why the sixteen is anomaly-free by construction. The rows above name particles, so they carry the particle's charges; a row written in the $\bar{\mathbf4}$ carries the negatives. §*One Naming Convention, Fixed Here* fixes the convention and states the difference properly.
- **A massive fermion needs both octets.** $e_L$ and $e_R$ are two cells and one electron at low energy; the electron is the Dirac combination of the two. So a count of *cells* is sixteen and a count of *particles* is fewer.
- **Three generations multiply the table by three**, so forty-eight Weyl fields and ninety-six states once the antiparticles of §*The Antiparticle Quantum Numbers* are counted. The number of generations is not fixed by the grid.

## The Conjugate Grid

**The sixteen rows above are every fermion of a generation, and the antiparticles are already inside them.** That is worth stating first, because the algebra invites the opposite reading. Charge conjugation maps the sixteen to a different representation, so the map cannot be read off the table by inspection, and the temptation is to add a second sixteen of fields. **No second multiplet is needed**: the antiparticle of a field is a conjugate mode of that same field, and the model contains no fermion that the sixteen lacks. What the map gives is a list of *quantum numbers* for the antiparticle states. This section writes that list out, because it is what fixes the charges of the antiparticles and the action of $C$ on the spectrum.

### The Operation

Charge conjugation on the algebra is

$$
Q^{\mathrm c}=-e_y\,\bar Q\,e_y ,
$$

coefficient conjugation followed by conjugation by the unit $e_y$. It is built in [Charge Conjugation and the Division Ring](../articles_physics/charge-conjugation-and-the-division-ring-charged-neutral-and-truly-neutral-particles-in-biquaternionic-form.html) and its consistency with the discrete symmetries is tested in [The CPT Theorem in Biquaternionic Form](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html). Two features of it decide what it does to the grid.

Conjugation by a unit is an inner automorphism, so it changes a basis and not a representation. The coefficient conjugation is the outer part, and it is outer on $\mathrm{SU}(4)$ and inner on $\mathrm{SU}(2)$: complex conjugation of a quaternion is conjugation by a pure unit, $j q j^{-1}$, so the doublet is its own conjugate and the quartet is not.

| property | test on the carrier | result |
|---|---|---|
| conjugate-linear | $C(iQ)=-i\,C(Q)$ | holds |
| an involution | $C(C(Q))=Q$ | holds |
| the left action | $C\,L_g\,C^{-1}=L_{C(g)}$ | holds for generic $g$ |
| the three imaginary units | $C(e_x)=-e_x$, $C(e_y)=+e_y$, $C(e_z)=-e_z$ | a rotation by $\pi$ about $e_y$ |
| the two chirality blocks | $E_\pm=\tfrac12(1\pm ie_z)$ | $C(E_\pm)=E_\pm$ |

**The last row is the statement that the antiparticle of a left-handed field is left-handed.** The operation is a rotation composed with a conjugation, and a rotation does not move a block. So the chirality of a cell survives, the doublet slot survives, and the quartet is reflected.

$$
C:\quad(\mathbf4,\mathbf2,\mathbf1)\longmapsto(\bar{\mathbf4},\mathbf2,\mathbf1),
\qquad
(\bar{\mathbf4},\mathbf1,\mathbf2)\longmapsto(\mathbf4,\mathbf1,\mathbf2).
$$

### The Antiparticle Quantum Numbers

Applied cell by cell, the map keeps the chirality block and the doublet slot, sends the colour index to its conjugate, and changes the sign of $Q$ and of $B-L$. The states so obtained for the left octet:

| antiparticle state | quartet index | $L$ index | $Q$ | $B-L$ |
|---|---|---|---|---|
| $\bar\xi_{\mathrm{neu},eL}$ | $\bar\xi_{\mathrm{neu}}$ | $\uparrow$ | $0$ | $+1$ |
| $\bar e_{L}$ | $\bar\xi_{\mathrm{neu}}$ | $\downarrow$ | $+1$ | $+1$ |
| $\bar u^{\bar r}_{L}$ | $\bar r$ | $\uparrow$ | $-\tfrac23$ | $-\tfrac13$ |
| $\bar d^{\bar r}_{L}$ | $\bar r$ | $\downarrow$ | $+\tfrac13$ | $-\tfrac13$ |
| $\bar u^{\bar g}_{L}$ | $\bar g$ | $\uparrow$ | $-\tfrac23$ | $-\tfrac13$ |
| $\bar d^{\bar g}_{L}$ | $\bar g$ | $\downarrow$ | $+\tfrac13$ | $-\tfrac13$ |
| $\bar u^{\bar b}_{L}$ | $\bar b$ | $\uparrow$ | $-\tfrac23$ | $-\tfrac13$ |
| $\bar d^{\bar b}_{L}$ | $\bar b$ | $\downarrow$ | $+\tfrac13$ | $-\tfrac13$ |

The right octet gives the same table with $R$ in place of $L$. So one rule covers all sixteen:

| the conjugate of | chirality | colour | $Q$ | $B-L$ |
|---|---|---|---|---|
| the left octet | $L$ | $\bar 3$ | $-Q$ | $-(B-L)$ |
| the right octet | $R$ | $\bar 3$ | $-Q$ | $-(B-L)$ |

**No row of this table is a new field.** Each row names one state of the field in the corresponding row of *The Fermions, on the Same Cells*, and that state is counted inside that field and not beside it. The table is therefore a table of numbers, and it adds nothing to the fermion content.

### The Count

| object | count |
|---|---|
| Weyl fields per generation | $16$ |
| states per generation | $32$ |
| particle states | $16$ |
| antiparticle states | $16$ |
| Weyl fields, three generations | $48$ |
| states, three generations | $96$ |

**The doubled number is a state count and not a field count.** Eight Dirac fields per generation — six quark fields, one per colour label, the electron and the neutrino — is $8\times2=16$ Weyl fields and $8\times4=32$ states, of which sixteen are particles and sixteen are antiparticles. Writing "thirty-two Weyl fields" would count every fermion twice, which is the error this paragraph exists to prevent.

### What Charge Conjugation Does Not Do

**$C$ is not a symmetry of this spectrum, and the article says so here rather than leaving a reader to assume the opposite.**

$$
C(S)=(\bar{\mathbf4},\mathbf2,\mathbf1)\oplus(\mathbf4,\mathbf1,\mathbf2)\;\neq\;S .
$$

The pair of multiplets is exchanged with a pair that is not the same pair. What closes the spectrum is $C$ composed with the exchange of the two weak factors, which is $CP$ in this frame because parity is the $L\leftrightarrow R$ swap:

| operation | $(\mathbf4,\mathbf2,\mathbf1)$ | $(\bar{\mathbf4},\mathbf1,\mathbf2)$ |
|---|---|---|
| $C$ | $(\bar{\mathbf4},\mathbf2,\mathbf1)$ | $(\mathbf4,\mathbf1,\mathbf2)$ |
| $CP$ with $L\leftrightarrow R$ | $(\bar{\mathbf4},\mathbf1,\mathbf2)$ | $(\mathbf4,\mathbf2,\mathbf1)$ |

**So the spectrum is closed under $CP$ and not under $C$, and that is the structural statement of left–right symmetry.** The model is not symmetric because its two weak factors happen to have equal couplings; it is symmetric because the sixteen is closed under the composed operation and not under either factor alone.

Two consequences follow, and both are already in the corpus without this argument.

The bidoublet is not an option. A fermion mass is the conversion of a cell into its conjugate, so it needs a scalar that carries both weak indices, which is exactly $(\mathbf1,\mathbf2,\mathbf2)$. The scalar sector of [The Scalar Sector](../articles_physics/the-scalar-sector-twenty-four-real-components-twelve-eaten.html) is the price of the conjugate grid.

The neutrino is not its own antiparticle here. $B-L$ is gauged and comes from inside $\mathrm{SU}(4)$, so a Majorana mass for $\xi_{\mathrm{neu},R}$ would break a gauged symmetry, and the renormalisable mass is the Dirac mass of the pair $\xi_{\mathrm{neu},L}$ and $\xi_{\mathrm{neu},R}$. That differs from the Standard Model, where a Majorana mass is available because $B-L$ is not gauged, and it is a statement the model makes rather than inherits.

### One Naming Convention, Fixed Here

**The same sixteen rows can be read two ways and the two readings disagree in the sign of $Q$ on eight of them.** Named as particles, a right-handed quark carries $Q=+\tfrac23$ and $B-L=+\tfrac13$. Placed in the $\bar{\mathbf4}$, whose weights are the negatives of the $\mathbf4$'s, the same cell carries $Q=-\tfrac23$. Neither reading is wrong; they are a name and a representation, and mixing them is what produces a table that contradicts itself.

The rule used in this article is one sentence: **a name denotes a particle, so every row of *The Fermions, on the Same Cells* carries the particle's own quantum numbers, and the conjugate rows carry the negatives.** The anomaly of the representations is then computed on $(\mathbf4,\mathbf2,\mathbf1)$ and $(\bar{\mathbf4},\mathbf1,\mathbf2)$, where the second block's entries are the conjugates of the named right-handed fields, which is why $+2-2=0$ rather than $+2+2$.

### What Is Measured

**The conjugate grid is not a prediction; it is a description of matter that has been observed since 1932.** The sharpest statements are comparisons, and they are listed because the model makes the equality exact.

| comparison | result |
|---|---|
| positron and electron, mass and charge | equal by the definition of the electron mass |
| antiproton and proton, $q/m$ | equal to a few parts in $10^{11}$ |
| $K^0$ and $\bar K^0$, masses | $\lvert m_{K^0}-m_{\bar K^0}\rvert<6.24\times10^{-48}$ kg |
| antihydrogen $1S$–$2S$ | agrees with hydrogen to $2\times10^{-12}$ |
| antihydrogen in free fall | acceleration agrees with $g$ to about $20$ per cent |
| antimatter in bulk | none beyond a few antihelium nuclei; baryon asymmetry $\digamma_{\mathrm{bau}}\approx6.1\times10^{-10}$ |

The equality of the first two rows is what $CPT$ forces and what the model's exact $CP$ closure reproduces cell by cell. The last row is the one thing the conjugate grid does not explain: the spectrum is symmetric under $CP$, and the universe is not.

## The Checks

| claim | check | result |
|---|---|---|
| the leptons per octet | $4$ quartet $\times$ $2$ doublet minus $6$ quarks | $2$ |
| the fermion count, as a product | $4\times2\times2$ | $16$ |
| the two fermion blocks | $4\times2\times1$ and $4\times1\times2$ | $8+8$ |
| the blocks against the product | $4\times2\times(1+1)$ | $16$ |
| the bifundamental | $\dim(\mathbf4,\mathbf2,\mathbf2)$ against the fermion content | both $16$, different objects |
| the fermions per generation | $8+8$ | $16$ |
| the conjugation, linearity | $C(iQ)$ against $-iC(Q)$ | conjugate-linear |
| the conjugation, involution | $C(C(Q))$ | $Q$ |
| the conjugation on the quartet | $C(e_x)$, $C(e_y)$, $C(e_z)$ | $-e_x$, $+e_y$, $-e_z$ |
| the chirality blocks | $E_\pm=\tfrac12(1\pm ie_z)$ under $C$ | preserved |
| the antiparticle states | rows, against the rows of *The Fermions, on the Same Cells* | $16$, each inside its own field |
| the Weyl fields per generation | $8$ Dirac $\times2$ | $16$ |
| the states per generation | $8$ Dirac $\times4$ | $32$ |
| the fields, three generations | $3\times16$ | $48$ |
| the states, three generations | $3\times32$ | $96$ |
| the $CP$ closure | $C$ composed with $L\leftrightarrow R$ | $S\mapsto S$ |
| the $C$ failure | $C(S)$ against $S$ | $\neq$ |

## Distinctions That Are Easy to Lose

$16=\dim(\mathbf4,\mathbf2,\mathbf2)$ is arithmetic and not content: the model's sixteen is two blocks of eight, with a singlet in each (*The Count Is a Product, Not a Sum of Squares*).

The two $2$'s are not the same $2$: one is a doublet's size, the other is the chirality block, and no fermion is a doublet of both weak groups at once (*The Count Is a Product, Not a Sum of Squares*).

A fermion row is not a grid cell: it is a quartet label times a doublet label, and the grids are shared with the bosons (*The Fermions, on the Same Cells*).

Sixteen cells is not sixteen particles: $e_L$ and $e_R$ are two cells of one electron (*The Fermions, on the Same Cells*).

Thirty-two is a state count, not a field count: the fields are sixteen per generation (*The Count*).

The antiparticle table adds no field: each row is a state of a field already in the sixteen (*The Antiparticle Quantum Numbers*).

A name carries the particle's charge and a representation carries the conjugate's: the same cell can be written $+\tfrac23$ or $-\tfrac23$ and only one is a name (*One Naming Convention, Fixed Here*).

$C$ does not close the spectrum; $CP$ with $L\leftrightarrow R$ does (*What Charge Conjugation Does Not Do*).

## Summary

**The count.** $4\times2\times2=16$, taken block by block as $4\times2\times1$ plus $4\times1\times2$, because one factor is a singlet in each block. **The fermions are the product of the model's three numbers; the bosons are their sum of squares.** The equality $16=\dim(\mathbf4,\mathbf2,\mathbf2)$ is arithmetic, and the block table is what tells the two objects apart.

**The fermions.** Sixteen per generation, a quartet index times a doublet index, and the colour is $\mathbf3$ on the left and $\bar{\mathbf3}$ on the right.

**The two octets.** The left octet is the quartet index times the $L$ grid's up/down; the right octet is the same indices times the $R$ grid, with the same $Q$ and $B-L$ and a different doublet grid.

**The antiparticles.** Charge conjugation is $-e_y\bar Qe_y$. It is inner on $\mathrm{SU}(2)$ and outer on $\mathrm{SU}(4)$, so it keeps the chirality block and reflects the quartet: $(\mathbf4,\mathbf2,\mathbf1)\mapsto(\bar{\mathbf4},\mathbf2,\mathbf1)$. The sixteen fields therefore already contain their own antiparticles, as conjugate modes; what the map supplies is the antiparticle charges, $Q\to-Q$, $B-L\to-(B-L)$, colour $\to\bar 3$. Sixteen fields per generation, thirty-two states, forty-eight fields and ninety-six states in three. The spectrum is closed under $CP$ with $L\leftrightarrow R$ and not under $C$, and that closure is the structural statement of left-right symmetry and the reason the bidoublet and the Dirac neutrino are not options.

**What it does not do.** It does not fix the number of generations, and it explains no mass: the conjugate grid is a description of matter, and the one thing it leaves out is why the universe carries more matter than antimatter.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\xi_{\mathrm{neu},eL}$, $\xi_{\mathrm{neu},eR}$ | the neutral lepton of the left and right doublets |
| $u^{\alpha}_{L}$, $d^{\alpha}_{L}$, $\alpha=r,g,b$ | the quark doublet in three colour copies |
| the left octet, the right octet | the eight fermions of one chirality block |
| $S$ | the representation $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$ |
| $C$ | charge conjugation, $Q^{\mathrm c}=-e_y\bar Qe_y$ |
| $E_\pm$ | the two chirality blocks, $\tfrac12(1\pm ie_z)$ |
| antiparticle state | a conjugate mode of a field, with the charges of §*The Antiparticle Quantum Numbers* |

## Further Reading

- [Classification of the Bosons: Twenty-Four Cells, Twenty-One Generators, One Name in Every Cell](classification-of-the-bosons-twenty-four-cells-twenty-one-generators-one-name-in-every-cell.html). The group, the three numbers, the ledger, the grid the fermions are read against, and the cells the bosons occupy.
- [Charge Conjugation and the Division Ring](../articles_physics/charge-conjugation-and-the-division-ring-charged-neutral-and-truly-neutral-particles-in-biquaternionic-form.html). Where $-e_y\bar Qe_y$ is built.
- [The CPT Theorem in Biquaternionic Form](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html). The consistency of the map with the discrete symmetries.
- [The Scalar Sector: Twenty-Four Real Components, Twelve Eaten, Twelve Surviving](the-scalar-sector-twenty-four-real-components-twelve-eaten.html). The bidoublet that the conjugate grid requires.
- [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html). Where the masses of these sixteen come from.
- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html). Why the neutrino here is Dirac and not Majorana.
- [The Excitation Ladder Theory of Flavour](the-excitation-ladder-theory-of-flavour.html). Why there are three generations, which the grid does not say.
