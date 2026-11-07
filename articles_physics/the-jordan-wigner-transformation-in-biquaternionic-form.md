# __The Jordan–Wigner Transformation in Biquaternionic Form__

## Introduction

A spin-$\tfrac12$ chain and a chain of fermionic modes obey different commutation rules, and in one dimension the two are one algebra read through two lists of generators. The change from one list to the other is the Jordan–Wigner transformation. In the biquaternion framework it has a sharp reading: the transformation is the **extension over sites of a one-site identity that is already inside the algebra**, and the object that extends it — the Jordan–Wigner string — is the product of the one-site parities, the element $i\vec e_z$ that the parents isolate in $\mathbb{B}_{\Psi}$.

This article establishes:

- **The one-site case is the algebra's own identity.** The ladder of a site is nilpotent, $\{\tilde S_{\Psi,+},\tilde S_{\Psi,-}\}=\frac{m^{2}\,c^{2}\,e_{t}}{k_m^{2}}$ and $[\tilde S_{\Psi,+},\tilde S_{\Psi,-}]=\frac{m^{2}\,c^{2}\,i\,\vec e_{z}}{k_m^{2}}$, so a one-site spin ladder *is* a fermionic mode with no string attached. There is nothing to transform at one site.
- **The string.** For $N$ sites the extension must carry a string, and the string is the tensor product of the one-site parities, $\prod_{k<j}i\vec e_z=\prod_{k<j}(-1)^{n_k}$. It lies in $\bigotimes_j\mathbb{B}_j$ and not in $\mathbb{B}$, and at one site it is the empty product, the identity.
- **The transformation, its parity and its nonlocality.** The two lists generate one algebra, of complex dimension $4^N$, and the change between them is the transformation. It respects the parity, which is one element on both lists, and it is not local: a one-site element of the spin list becomes a string-laden element of the mode list. The transformation is a choice of square root of the chain algebra, and the ordering of the sites is the branch.
- **The consequences.** The hopping identity, the number and parity identities, the inverse map, the free solution of the XY chain, and the boundary term that distinguishes the two parity sectors.

The standard material is transcribed with explicit signs; the biquaternion content is the one-site identity and the parity reading of the string.

$$
\boxed{\;\tilde C_j=\frac{k_m\,\tilde{Z}_{<j}\,\tilde{S}_{\Psi,+,j}}{m\,c} ,
\qquad
\tilde Z_{<j}=\prod_{k<j}\tilde Z_k ,
\qquad
\tilde S_{\Psi,\pm,j}=\tilde S_{\Psi,x,j}\pm  i\tilde S_{\Psi,y,j}\;},
$$

with $\tilde Z_k=i\vec e_z$ the parity of site $k$ and the spin-down value $\tilde Z_k=-1$ occupied. A symbol carrying one site subscript is the element of that site tensored with the identities of the others, so the second subscript is a site label and not a tensor index. Every identity below is an identity between elements of the chain algebra, and each was verified by exact computation on chains of up to four sites.

## The One-Site Case

The chain's algebra contains a fermionic mode, and it contains it with no string and no extension. The spin of a site is $\tilde S_{\Psi,k}=\frac{m\,c}{2\,k_m}i\vec e_k$, the element the conventions fix (*Algebra and Element Conventions*, §*The Observables, the States and the Quantum Objects*), and the ladder is the derived pair

$$
\tilde S_{\Psi,+}=\tilde S_{\Psi,x}+i\tilde S_{\Psi,y}=\frac{m\,c}{2\,k_m}\bigl(i\vec e_x-\vec e_y\bigr) ,
\qquad
\tilde S_{\Psi,-}=\tilde S_{\Psi,x}-i\tilde S_{\Psi,y}=\frac{m\,c}{2\,k_m}\bigl(i\vec e_x+\vec e_y\bigr) .
$$

**The two squares vanish, and the two products are two elements of $\mathbb{B}_{\Psi}$.** From $i^2=-1$, $\vec e_x^2=\vec e_y^2=-e_t$ and $\vec e_x\vec e_y=-\vec e_y\vec e_x=\vec e_z$,

$$
(i\vec e_x\pm\vec e_y)^2=i^2\vec e_x^2\pm i\bigl(\vec e_x\vec e_y+\vec e_y\vec e_x\bigr)+\vec e_y^2=(-1)(-e_t)\pm0-e_t=0 ,
$$

$$
\tilde S_{\Psi,+}\tilde S_{\Psi,-}=\frac{m^{2}\,c^{2}}{4\,k_m^{2}}\bigl(i^2\vec e_x^2+i\vec e_x\vec e_y-i\vec e_y\vec e_x-\vec e_y^2\bigr)=\frac{m^{2}\,c^{2}}{2\,k_m^{2}}\bigl(e_t+i\vec e_z\bigr) ,
\qquad
\tilde S_{\Psi,-}\tilde S_{\Psi,+}=\frac{m^{2}\,c^{2}}{2\,k_m^{2}}\bigl(e_t-i\vec e_z\bigr) .
$$

Summing the two products gives the anticommutator, subtracting them gives the commutator, and each square vanishes:

$$
\boxed{\;\tilde S_{\Psi,+}^2=0 ,
\qquad
\tilde S_{\Psi,-}^2=0 ,
\qquad
\{\tilde S_{\Psi,+},\tilde S_{\Psi,-}\}=\frac{m^{2}\,c^{2}\,e_{t}}{k_m^{2}},
\qquad
[\tilde S_{\Psi,+},\tilde S_{\Psi,-}]=\frac{m^{2}\,c^{2}\,i\,\vec e_{z}}{k_m^{2}}}.
$$

**The pair is fermionic, and the commutator is not central.** The anticommutator is a multiple of the identity and the commutator is not: the centre of $\mathbb{B}$ is $\mathbb{C}e_t$, while $i\vec e_z$ is a Hermitian element of $\mathbb{B}_{\Psi}$ outside it. The ladder therefore cannot satisfy a bosonic relation with a scalar right-hand side, and there is nothing here to bosonize. Two nilpotent elements that anticommute to the identity are all the algebra needs for one mode.

**The one-site transformation is an identity.** The mode of one site is $\frac{k_m\,\tilde{S}_{\Psi,+}}{m\,c}$. This is the one-site Jordan–Wigner transformation, and it is an identity inside $\mathbb{B}$ rather than a transformation: the spin ladder and the mode are one element. The reason it needs no string is structural — the string is a product of the *other* sites' parities, and at one site there are no other sites, so the product is empty and equals $e_t$. The algebra's contribution to the story is therefore not the string but the fact that the transformation has a one-site fixed point: the spin and the mode are two readings of one element, and a difference appears only when a *second* site is present.

## The Declared Axis

**The chain declares one spatial unit.** The spin of a site is measured along a direction the chain supplies, and that direction is the article's only named unit. Write $\vec u$ for it. Nothing in the algebra privileges one of the three spatial units; the chain does, once, at the outset, by declaring its axis. Every statement below that holds for a declared unit is written in $\vec u$, so that no unit is privileged by the notation itself. The chain measures along the third coordinate direction, so its declared unit is $\vec u=\vec e_z$, and the body writes $\vec e_z$ only where that concrete direction enters a formula.

**An operator is diagonal in a basis when each basis element is carried into a multiple of itself.** Of the sixteen cells, four are diagonal in each of the two bases of this article, and the two fours are different. In the coefficient basis they are the four squares,

$$
e_t e_t ,\qquad \vec e_x\vec e_x ,\qquad \vec e_y\vec e_y ,\qquad \vec e_z\vec e_z ,
$$

and that set is unchanged by any permutation of the three spatial units. In the frame built on the declared unit — the frame the closing section prints in the $\mathrm{pau}$ display, whose four vectors are the four columns of $C_\Pi$ — they are the four products whose two multipliers lie in $\{e_t,\vec u\}$,

$$
e_t e_t ,\qquad e_t\vec u ,\qquad \vec u e_t ,\qquad \vec u\vec u ,
$$

the row naming the declared unit and the time unit and no other spatial unit at all. Three of the four carry a time slot, and a cell with a time slot collapses, because $e_t$ is the unit: the four are the identity, right multiplication by $\vec u$, left multiplication by $\vec u$, and the two-sided $\vec u[\,]\vec u$. That set therefore changes when the units are permuted, and the coefficient-basis four do not.

**The site parity is diagonal in the frame built on the declared unit.** Right multiplication by $i\vec u$ carries each of the four elements of that frame into a multiple of itself, $+1$ on two of them and $-1$ on the other two, and it is not diagonal in the coefficient basis, where it carries a coefficient unit into a combination of the other units. This is the only role the axis plays below: the string multiplies one such parity per site, so it is diagonal in the frame built on the declared unit and not in the coefficient basis, and that is a property of the basis and not of the algebra.

**A change of display keeps every invariant.** The two bases are carried into one another by the conjugation $C_\Pi$ (*Matrix Representations Conventions*, §*The Switch Between the Two Frames*), and a conjugation by $C_\Pi$ changes no product, no commutator, no trace and no determinant. Every identity below is therefore a statement about elements, and it holds in both displays; the closing section prints one of them beside the other.

**Chirality is the subscript, and it takes two values.** An element is written $\tilde Q_L$ or $\tilde Q_R$: $\tilde Q_L$ is the element of value the minus one and $\tilde Q_R$ the element of value the plus one, and that is the whole definition. The two values are exactly two, and only the zero element carries both. The subscript is a function of the element and of the declared axis; a product takes the letter of its right factor, and left multiplication keeps the letter (*Special Element Conventions*, §*The Chirality Convention*). In this article the two values name the parts of the field of the closing section, $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$, and no other object of the article carries them.

## The Many-Site Map

Let the chain carry $N$ sites, with chain algebra $\bigotimes_{j=1}^N\mathbb{B}_j$ and identity $e_t$. A symbol carrying one site subscript is the element of that site tensored with the identities of the others, so $\tilde S_{\Psi,\alpha,j}$ is $\tilde S_{\Psi,\alpha}$ of site $j$ and $\tilde Z_j$ is $i\vec e_z$ of site $j$.

**The mode and its star.** Define, for $j=1,\dots,N$,

$$
\tilde C_j=\Bigl(\prod_{k<j}\tilde Z_k\Bigr)\frac{k_m\,\tilde{S}_{\Psi,+,j}}{m\,c} ,
\qquad
\tilde C_j^{*}=\Bigl(\prod_{k<j}\tilde Z_k\Bigr)\frac{k_m\,\tilde{S}_{\Psi,-,j}}{m\,c} ,
$$

with $\tilde Z_{<j}=\prod_{k<j}\tilde Z_k$ the string of site $j$ and $\tilde Z_{<1}=e_t$. The second is the star of the first, because $\tilde Z_k^{*}=\tilde Z_k$ and $\tilde S_{\Psi,+,j}^{*}=\tilde S_{\Psi,-,j}$. The string is a product of parities, hence Hermitian and of square the identity,

$$
\tilde Z_{<j}^{*}=\tilde Z_{<j} ,
\qquad
\tilde Z_{<j}^{\,2}=e_t .
$$

The literature writes the same mode as the Fock operator $c_{\mathrm{fop},j}$ with its adjoint $c_{\mathrm{fop},j}^{\dagger}$; the identities below are identities between elements of the chain algebra, and the transcription to that notation is the standard one.

**The anticommutators.** Three identities follow, and all three were verified by exact computation on chains of up to four sites:

$$
\boxed{\;\{\tilde C_i,\tilde C_j\}=0 ,
\qquad
\{\tilde C_i,\tilde C_j^{*}\}=\delta_{ij}\,e_t\;}.
$$

The cancellation of the string requires that the two sites be ordered. For $i<j$ the string of $\tilde C_j$ carries the parity of every site below $j$; in the product $\tilde C_i\tilde C_j$ the factors below $i$ commute past $\tilde S_{\Psi,+,i}$ and cancel the string of $\tilde C_i$, which leaves $\tilde Z_i$ immediately to the right of $\tilde S_{\Psi,+,i}$, and $\tilde S_{\Psi,+,i}\tilde Z_i=-\tilde S_{\Psi,+,i}$ is the whole sign. The factors with $i<k<j$ commute with $\tilde S_{\Psi,+,i}$ and cost nothing, which is why the string cancels for every pair of sites and not only for adjacent ones.

**The number and the parity.** With the sign convention above,

$$
\tilde N_j:=\tilde C_j^{*}\tilde C_j=\tfrac12\bigl(e_t-\tilde Z_j\bigr) ,
\qquad
\tilde Z_j=e_t-2\tilde N_j ,
$$

so the occupied value is the spin-down value, $\tilde Z_j=-1$ and $\tilde N_j=1$, and the parity of a site *is* the site's own $\tilde Z_j$: the two readings are of one element, and the site's two values of $\tilde N_j$ are $0$ and $1$ exactly where those of $\tilde Z_j$ are $+1$ and $-1$, in that order.

**The hopping and the inverse.** The quadratic elements reproduce the XY coupling,

$$
\tilde C_j^{*}\tilde C_{j+1}+\tilde C_{j+1}^{*}\tilde C_j
=\tfrac12\Bigl((i\vec e_x)_j(i\vec e_x)_{j+1}+(i\vec e_y)_j(i\vec e_y)_{j+1}\Bigr)
=-\tfrac12\Bigl((\vec e_x)_j(\vec e_x)_{j+1}+(\vec e_y)_j(\vec e_y)_{j+1}\Bigr) ,
$$

and the inverse returns the spin elements,

$$
(i\vec e_x)_j=\tilde Z_{<j}\bigl(\tilde C_j+\tilde C_j^{*}\bigr) ,
\qquad
(i\vec e_y)_j=-i\,\tilde Z_{<j}\bigl(\tilde C_j-\tilde C_j^{*}\bigr) ,
\qquad
(i\vec e_z)_j=e_t-2\tilde N_j .
$$

Both were verified bond by bond and site by site on the four-site chain. The inverse displays the asymmetry of the transformation: recovering a spin element requires the same string that the mode carried, so the change is between two lists of one algebra, and the *mode* is defined only relative to an ordering of the sites.

### The String Is a Product of One-Site Parities

The string is not a novel object. It is the product of the parities of the sites to its left,

$$
\tilde Z_{<j}=\prod_{k<j}\tilde Z_k=\prod_{k<j}(-1)^{n_k} ,
\qquad
(-1)^{n}=i\vec e_z=\frac{2\,k_m\,\tilde{S}_{\Psi,z}}{m\,c} ,
$$

the one-site factor being the parity element the parents isolate in $\mathbb{B}_{\Psi}$. The Jordan–Wigner string is therefore the tensor product of the one-site biquaternion parities,

$$
\tilde Z_{<j}\;\in\;\bigotimes_{k=1}^{j-1}\mathbb{B}_k ,
$$

one factor of $i\vec e_z$ per site to the left. This is the biquaternion content of the transformation, and it explains both of its structural features at once.

- **Why one site needs no string.** The empty product of one-site parities is the identity, and the one-site map is the identity of the previous section.
- **Why the string is not in $\mathbb{B}$.** For $N\ge2$ the string is a tensor product with at least one nontrivial factor, so it lies outside the diagonal copy of $\mathbb{B}$ in $\bigotimes_j\mathbb{B}_j$; the algebra has no way to express a parity of *another* site. The grading that the spin–statistics companion records as external for the field is, for the chain, exactly the string.

## The Map as a Change of Generators and Its Grading

**The two lists generate one algebra.** The $3N$ spin elements $\tilde S_{\Psi,k,j}$ generate the chain algebra, and so do the $2N$ elements $\tilde C_j,\tilde C_j^{*}$: each mode is a product of spin elements, and the inverse above returns the spin elements from the modes. The chain algebra has complex dimension $4^N$, the dimension of $N$ copies of $\mathbb{B}$, and the generation was verified by rank computation for $N=1$ (dimension $4$) and $N=2$ (dimension $16$). The transformation is the change from the first list to the second, inside one algebra; it is invertible and it is unital.

**It respects the parity and it does not preserve locality.** The whole-chain parity is the product of the site parities,

$$
\prod_{j=1}^N\tilde Z_j ,
$$

one element, the same on both lists: the transformation does not transport it, because there is nothing to transport. Call an element *even* when it commutes with that product and *odd* when it anticommutes with it. Then each $\tilde Z_j$ is even, each mode is odd, and each product $\tilde C_i^{*}\tilde C_j$ is even. What the change of lists does not preserve is the site structure: a one-site spin element becomes an element carrying the string of every site to its left, and a one-site mode becomes a string times a raising element. Locality is lost in both directions.

**The transformation is a choice of square root.** The modes are odd elements and their products span the elements that commute with the whole-chain parity: at $N=2$ those form an algebra of complex dimension $8$, while the number bilinears $\tilde C_i^{*}\tilde C_j$ alone generate one of dimension $6$, so the pairing bilinears $\tilde C_i\tilde C_j$ and $\tilde C_i^{*}\tilde C_j^{*}$ are needed with them. Passing from the spin list to the mode list is taking a square root of the algebra — the modes are the odd generators, and their products span the even part — and the string is the choice of branch. It is also why the change cannot be canonical: a square root has a branch, and the branch is the ordering of the sites.

## Consequences for the Chain

**Free modes.** The hopping identity converts the XY coupling into a quadratic form. The spin form is

$$
\boxed{\;H_{XY}=-J\sum_j\Bigl((\vec e_x)_j(\vec e_x)_{j+1}+(\vec e_y)_j(\vec e_y)_{j+1}\Bigr)\;}
$$

and the mode form, equal to it term by term through the hopping identity, is

$$
H_{XY}=2J\sum_j\Bigl(\tilde C_j^{*}\tilde C_{j+1}+\tilde C_{j+1}^{*}\tilde C_j\Bigr) ,
$$

which is free in the modes, diagonalised by a Bogoliubov transformation in momentum space. The transverse-field Ising chain is brought to the same form up to a pairing term $\tilde C_j\tilde C_{j+1}+\tilde C_j^{*}\tilde C_{j+1}^{*}$, which a Majorana decomposition absorbs. The transcription is standard and is recorded as such; the biquaternion framework adds nothing to the solution.

**A two-site example.** For $N=2$ the identity can be exhibited in full. The two sides

$$
-J\bigl((\vec e_x)_1(\vec e_x)_2+(\vec e_y)_1(\vec e_y)_2\bigr)
=2J\bigl(\tilde C_1^{*}\tilde C_2+\tilde C_2^{*}\tilde C_1\bigr)
$$

are one element, with spectrum $\{-2J,0,0,+2J\}$ — a non-degenerate lowest value, a non-degenerate highest, and a doubly degenerate level at zero, which is the free spectrum of two modes with the hopping turned on. The whole-chain parity $\tilde Z_1\tilde Z_2$ commutes with the element, with commutator equal to the zero element, so the two parity values separate the spectrum. The zero level is even — it holds the empty configuration and the doubly occupied one — while the values $\mp2J$ are odd. The degeneracy at zero is therefore the particle–hole pairing of the free theory and not a parity degeneracy: the parity does not resolve it.

### The String as a Cocycle

The string has one more structural property that the spin language hides and the mode language makes plain: it is a multiplicative one-cocycle of the site ordering. With $\tilde Z_{<j}=\prod_{k<j}\tilde Z_k$, the increment from one site to the next is that site's own parity,

$$
\tilde Z_{<j+1}=\tilde Z_{<j}\tilde Z_j ,
\qquad
\tilde Z_{<j}\tilde Z_{<i}^{-1}=\prod_{i\le k<j}\tilde Z_k\quad(i<j) ,
$$

so the relative string of two sites is the parity of the interval between them. Three things follow. The modes anticommute, $\tilde C_i\tilde C_j=-\tilde C_j\tilde C_i$ for $i\ne j$, and the sign is the single element $\tilde Z_i$ that the longer string carries beside a raising element. Each mode is defined only relative to the ordering, since $\tilde C_j$ carries the parity of every site to its left. And the transformation is nonlocal for a reason the cochain makes visible: an element supported on one site of the spin list is supported on that site and on every site to its left in the mode list.

The biquaternion reading is the same as before: the increments of the cochain are the one-site parities $\tilde Z_k=i\vec e_z$, so the relative string of two sites is the tensor product of that many factors of the algebra's parity, and the cocycle condition is the statement that these products multiply consistently.

**The boundary term.** The string makes the transformation nonlocal, and the nonlocality has a physical place: it sits at the chain's ends. The whole-chain parity $\prod_j\tilde Z_j$ is the product of the on-site parities and commutes with $H_{XY}$; the two values it takes label the two boundary conditions for the modes. In the ordered phase of the transverse-field Ising chain the two lowest levels of the two sectors are nearly degenerate, and that near-degeneracy is the standard signature of the $\mathbb{Z}_2$ symmetry of the spin language and of the two boundary-condition sectors of the mode language.

**The hidden symmetry.** The transformation also shows why an element that is simple in one list need not be simple in the other: the parity is the product of on-site parities, the occupation is the sum of the site numbers $\tilde N_j$, and the hopping is a two-site product in the spin list and a bilinear in the modes. The transformation creates no symmetry and destroys none; it relabels which generators are simple.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The Jordan–Wigner transformation itself, the string, the anticommutators, the number and parity identities, the hopping identity, the inverse map, the free solution of the XY and transverse-field Ising chains, and the boundary-condition sectors. This is textbook material in the stated convention, and every sign was recomputed on chains up to $N=4$.

**The algebra's own.**

- *The one-site identity.* The ladder of a site is a pair of nilpotents with $\{\tilde S_{\Psi,+},\tilde S_{\Psi,-}\}=\frac{m^{2}\,c^{2}\,e_{t}}{k_m^{2}}$ inside $\mathbb{B}$, and the transformation has a one-site fixed point.
- *The string as the product of one-site parities.* $\prod_{k<j}\tilde Z_k$, with $\tilde Z_k=i\vec e_z$ the parity element of a site. The string is the tensor product of the parities of the algebra, and its non-diagonality is the external grading the spin–statistics companion records.
- *The parity statement.* The parity is one element, $\prod_j\tilde Z_j$, on both lists, and the transformation respects it: the site parities are even and the modes are odd. What the transformation does not preserve is the site structure, since a one-site spin element becomes a string-laden mode element.
- *The declared axis.* The parity is diagonal in the frame built on the declared unit and not in the coefficient basis, and the diagonal products of the two bases are different fours. The axis is a property of the basis, and no unit is privileged by the algebra.

**Open.**

- **The chain and the field.** The chain's transformation is between two lists of generators of one finite-dimensional algebra; the field's grading remains external, as the spin–statistics companion records, and no continuum version of the string is adopted here.
- **Boundary conditions in the continuum.** The relation between the chain's two parity sectors and the field's boundary conditions is standard for the lattice and is not pushed to the continuum here.
- **The uniqueness of the square root.** The transformation is one choice of square root of the algebra; whether the algebra singles out a preferred ordering, and hence a preferred string, is not determined by anything used here.

## Companion Articles

- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder identified here with the one-site spin, and the parity $i\vec e_z$.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the two displays of one element and the conjugation $C_\Pi$ that carries one into the other.
- Companion article *Biquaternion Physical Interpretation of Operator Chirality*, for the definition of chirality as the side on which an operator multiplies; the closing section prints its cell.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are cells of the same two-sided operator algebra that the one-site identification used, and the chirality cell is the right multiplication by $\vec e_z$ that separated the two carriers there.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

The four frame cells are the four coordinates, with the factor $i$ belonging to the cell:

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\qquad
\gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\qquad
\gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}.
$$

The fifth gamma is not a fifth frame vector but their product, and $i^2=-1$ fixes its sign and its cell. Multiplying cells, $L_aR_b\,L_cR_d=L_{ac}R_{db}$, with $\vec e_x\vec e_x=\vec e_y\vec e_y=-e_t$ and $\vec e_x\vec e_y=-\vec e_y\vec e_x=\vec e_z$,

$$
\gamma_0\gamma_1\gamma_2\gamma_3=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z},
\qquad
\gamma_5:=i\gamma_0\gamma_1\gamma_2\gamma_3=i\bigl(-L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}\bigr)=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}=-iR_{\mathrm{pau},\vec e_z}.
$$

In the axis-free display:

$$
\gamma_0\gamma_1\gamma_2\gamma_3=-L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z},
\qquad
\gamma_5:=i\gamma_0\gamma_1\gamma_2\gamma_3=i\bigl(-L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}\bigr)=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}=-iR_{\mathrm{axf},\vec e_z}.
$$

The four gammas carry $i^4=1$, so the single $i$ of the definition survives, and no second factor of $i$ is left over: the cell that results is $-iR_{\mathrm{pau},\vec e_z}$, in which the left multiplier is the identity and the cell has collapsed to a right multiplication.

That right multiplication is the one the one-site section met, up to the factor $i$: the Peirce sign of the two carriers is $P=R_{\mathrm{pau},i\vec e_z}=iR_{\mathrm{pau},\vec e_z}$, so

$$
\gamma_5=-iR_{\mathrm{pau},\vec e_z}=-P ,
\qquad
P^2=I_4 ,
$$

The same identities in the axis-free display:

$$
\gamma_5=-iR_{\mathrm{axf},\vec e_z}=-P ,
\qquad
P^2=I_4 ,
$$

and the two differ only by the overall sign that the frame fixes. The Peirce sign is a copy index inside $\mathbb{B}$; the chirality is not. The cell is $-iR_{\mathrm{axf},\vec e_z}$, a pure right multiplier, and its side is the right slot; its central form is the sign $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ of the complexified algebra.

The frame is Clifford, with $\varepsilon=(1,-1,-1,-1)$ and $I_4=L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}$ the identity cell:

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4 ,
\qquad
\gamma_5^2=I_4 ,
\qquad
\{\gamma_\mu,\gamma_5\}=0 ,
\qquad \varepsilon=(1,-1,-1,-1),$$

all three checked cell by cell.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$. The central grading is a different object and carries its own factors: $\tilde{Ζ}_{\mathrm{ad}}$ is the central root of the double with $\tilde{Ζ}_{\mathrm{ad}}^2=-e_t$, so $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ has

$$
\xi^2=i^2\tilde{Ζ}_{\mathrm{ad}}^2=(-1)(-e_t)=e_t ,
$$

and $\xi$ is the difference of the two central idempotents of the complexified algebra, $(e_t+\xi)/2-(e_t-\xi)/2=\xi$. The cell represents $\xi$ on the Dirac module; it is not its definition. The chirality pairs the two halves of that module, and the field article writes the pair as two equations, one for each chirality:

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L} ,
$$

$$
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R} .
$$

Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The two act from the left; what separates them is the conjugation $\natural$, not a change of side. The mass is the one term of the pair that mixes the two chiralities.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Jordan–Wigner transformation in biquaternion form has a one-site fixed point inside the algebra and is extended over sites by the product of the algebra's parities. At one site the ladder $\tilde S_{\Psi,\pm}=\frac{m\,c}{2\,k_m}(i\vec e_x\mp\vec e_y)$ satisfies $\tilde S_{\Psi,\pm}^2=0$, $\{\tilde S_{\Psi,+},\tilde S_{\Psi,-}\}=\frac{m^{2}\,c^{2}\,e_{t}}{k_m^{2}}$ and $[\tilde S_{\Psi,+},\tilde S_{\Psi,-}]=\frac{m^{2}\,c^{2}\,i\,\vec e_{z}}{k_m^{2}}$, so a one-site spin ladder *is* a fermionic mode and the string is the empty product.

For $N$ sites, with $\tilde C_j=\frac{k_m\,\tilde{Z}_{<j}\,\tilde{S}_{\Psi,+,j}}{m\,c}$ and the spin-down value occupied,

$$
\{\tilde C_i,\tilde C_j^{*}\}=\delta_{ij}\,e_t ,
\qquad
\{\tilde C_i,\tilde C_j\}=0 ,
\qquad
\tilde N_j=\tfrac12\bigl(e_t-\tilde Z_j\bigr) ,
\qquad
\tilde Z_j=e_t-2\tilde N_j ,
$$

$$
\tilde C_j^{*}\tilde C_{j+1}+\tilde C_{j+1}^{*}\tilde C_j
=-\tfrac12\bigl((\vec e_x)_j(\vec e_x)_{j+1}+(\vec e_y)_j(\vec e_y)_{j+1}\bigr) ,
$$

all verified with zero error on chains of up to four sites. The string is the product of the one-site parities, $\prod_{k<j}\tilde Z_k=\prod_{k<j}(-1)^{n_k}$, each factor being the parity element $i\vec e_z$; it is the identity at one site and non-diagonal beyond, which is the same externality of the grading that the spin–statistics companion records for the field.

The transformation is a change of generators of one algebra — both lists generate the whole algebra, of complex dimension $4^N$, verified by rank computation for $N=1,2$ — it respects the parity, and it is not local: a one-site spin element becomes a string-laden mode element, the modes are the odd elements whose products span the even part, and the ordering of the sites is the branch. The consequences are the standard ones: the XY chain becomes free modes, the whole-chain parity $\prod_j\tilde Z_j$ labels the two boundary-condition sectors, and the near-degeneracy of the ordered phase appears as the standard $\mathbb{Z}_2$ structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde S_{\Psi,k}=\frac{m\,c}{2\,k_m}i\vec e_k$, $\tilde S_{\Psi,\pm}=\frac{m\,c}{2\,k_m}(i\vec e_x\mp\vec e_y)$ | Spin of a site; the ladder is derived from it |
| $\tilde S_{\Psi,\pm}^2=0$, $\{\tilde S_{\Psi,+},\tilde S_{\Psi,-}\}=\frac{m^{2}\,c^{2}\,e_{t}}{k_m^{2}}$, $[\tilde S_{\Psi,+},\tilde S_{\Psi,-}]=\frac{m^{2}\,c^{2}\,i\,\vec e_{z}}{k_m^{2}}$ | Canonical anticommutator inside the algebra; the commutator is not central |
| $\tilde Z_j=i\vec e_z$ at site $j$ | Parity of a site, $=\frac{2\,k_m\,\tilde{S}_{\Psi,z,j}}{m\,c}=(-1)^{n_j}$ |
| $\tilde Z_{<j}=\prod_{k<j}\tilde Z_k$ | The string, $e_t$ at $j=1$; Hermitian, of square $e_t$ |
| $\tilde C_j=\frac{k_m\,\tilde{Z}_{<j}\,\tilde{S}_{\Psi,+,j}}{m\,c}$, $\tilde C_j^{*}=\frac{k_m\,\tilde{Z}_{<j}\,\tilde{S}_{\Psi,-,j}}{m\,c}$ | Mode and its star |
| $\{\tilde C_i,\tilde C_j\}=0$, $\{\tilde C_i,\tilde C_j^{*}\}=\delta_{ij}e_t$ | Canonical anticommutators (verified, error $0$) |
| $\tilde N_j=\tilde C_j^{*}\tilde C_j=\tfrac12(e_t-\tilde Z_j)$ | Occupation of a site |
| $\prod_j\tilde Z_j$ | Whole-chain parity; boundary-condition sectors |
| $H_{XY}=-J\sum_j((\vec e_x)_j(\vec e_x)_{j+1}+(\vec e_y)_j(\vec e_y)_{j+1})$ | XY chain, $=2J\sum_j(\tilde C_j^{*}\tilde C_{j+1}+\text{h.c.})$ |
| $e_te_t$, $e_t\vec u$, $\vec u e_t$, $\vec u\vec u$ | The four diagonal cells of the frame built on the declared unit; $\vec u$ is the declared unit, $\vec u=\vec e_z$ for this chain |
| $\tilde Q_L,\tilde Q_R$ | The two values of the chirality subscript, minus and plus |
| $C_\Pi$ | The conjugation that carries one display into the other |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot," *Zeitschrift für Physik* **47** (1928) 631–651, for the transformation itself.
- E. Lieb, T. Schultz and D. Mattis, "Two soluble models of an antiferromagnetic chain," *Annals of Physics* **16** (1961) 407–466, for the free-fermion solution of the XY and Ising chains by the transformation.
- P. Pfeuty, "The one-dimensional Ising model with a transverse field," *Annals of Physics* **57** (1970) 79–90, for the transverse-field Ising chain, its two sectors and its degeneracy.
- J. B. Kogut, "An introduction to lattice gauge theory and spin systems," *Reviews of Modern Physics* **51** (1979) 659–713, for the Jordan–Wigner string, the boundary conditions and the $\mathbb{Z}_2$ structure.
- S. Sachdev, *Quantum Phase Transitions* (Cambridge, 2011), for the transverse-field Ising chain and the one-dimensional $\mathbb{Z}_2$ physics used here.
- E. Fradkin, *Field Theories of Condensed Matter Physics* (Cambridge, 2013), for the Jordan–Wigner transformation in the many-body setting and the nonlocal string.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the Clifford algebra with the fermionic mode algebra and the even/odd splitting.
- K. Huang, *Statistical Mechanics* (Wiley, 1987), and R. B. Griffiths, "Correlations in Ising ferromagnets," *Journal of Mathematical Physics* **8** (1967) 478–483, for the $\mathbb{Z}_2$ symmetry and its consequences in the chain.
