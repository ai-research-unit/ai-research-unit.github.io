# __The Jordan–Wigner Transformation in Biquaternionic Form__

## Introduction

A spin-$\tfrac12$ chain and a chain of fermionic modes are described by different operators with different commutation rules, and yet in one dimension the two descriptions carry the same state space and the same algebra. The map between them is the Jordan–Wigner transformation. In the biquaternion framework it has a sharp interpretation: the transformation is the **extension over sites of a one-site identity that is already inside the algebra**, and the object that extends it — the Jordan–Wigner string — is the product of the one-site fermionic parities, the element $(-1)^F=i\vec e_z$ that the parents isolate in $\mathbb{M}_+$.

This article establishes:

- **The one-site case is the algebra's own identity.** For one mode the parents' ladder $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ satisfies $\vec\Upsilon_x^2=0$ and $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ inside $\mathbb{B}$, so a one-site spin ladder *is* a fermionic mode with no string attached. The spin generators are the bilinears $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, and the ladder they build is the same pair, $\tilde S_+=\hbar\,\vec\Upsilon_x$ and $\tilde S_-=\hbar\,\vec\Upsilon_y$. There is nothing to transform at one site.
- **The string.** For $N$ sites the map must carry a string, and the string is exactly the tensor product of the one-site parities: $\prod_{k<j}(-1)^{n_k}=\prod_{k<j}(\sigma_z)_{k}$, with $n_k$ the occupation of the site. It lies in $\bigotimes_j\mathbb{B}$ but not in $\mathbb{B}$, and for one site it collapses to the identity, which is why the one-site case needed none.
- **The map, its grading and its nonlocality.** The Jordan–Wigner map is a unital algebra isomorphism between the spin algebra and the fermionic mode algebra — both are the full matrix algebra of the $2^N$-dimensional space, and this is the Clifford identity $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$. It **does** preserve the parity grading, because $(-1)^{F}=\prod_j(\sigma_z)_{j}$ is the same operator on the two sides: $(\sigma_z)_{j}$ is even, $(\sigma_x)_{j}$ and $(\sigma_y)_{j}$ are odd, and the modes $c^{\mathrm{fop}}_j$ are odd. What it does not preserve is locality: a one-site spin operator becomes a string-laden fermion operator, and conversely. The transformation is the choice of a square root of the spin algebra, and the string is its branch cut.
- **The consequences.** The hopping identity, the parity identity, the inverse map, the free-fermion solution of the XY chain, and the boundary term that distinguishes the two fermion-parity sectors.

The standard material is transcribed with explicit signs; the biquaternion content is the one-site identification and the parity interpretation of the string.

$$
\boxed{\;c^{\mathrm{fop}}_j=\Big(\prod_{k<j}(\sigma_z)_{k}\Big)(\sigma_+)_{j} ,
\qquad
(\sigma_\pm)_{j}=\tfrac12\big((\sigma_x)_{j}\pm i(\sigma_y)_{j}\big)\;},
$$

with the spin-down state ($\sigma_z=-1$) occupied. Here $(\sigma_\alpha)_{j}$ is $\sigma_\alpha$ on site $j$ and the identity everywhere else; the outer subscript is a site label, not a tensor index. All signs below are in this convention and were verified by exact matrix computation on chains up to $N=4$.

## The One-Site Case

The biquaternion algebra contains a fermionic mode, and it contains it with no string and no extension. Write

$$
\vec\Upsilon_x=\tfrac12\big(i\vec e_x-\vec e_y\big),
\qquad
\vec\Upsilon_y=\tfrac12\big(i\vec e_x+\vec e_y\big),
$$

as the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* defines them. The two squares follow from $i^2=-1$, $\vec e_x^2=\vec e_y^2=-e_t$ and $\vec e_x\vec e_y=-\vec e_y\vec e_x=\vec e_z$:

$$
(i\vec e_x\pm\vec e_y)^2=i^2\vec e_x^2\pm i\bigl(\vec e_x\vec e_y+\vec e_y\vec e_x\bigr)+\vec e_y^2=(-1)(-e_t)+0-e_t=0 ,
$$

and the two products are the Peirce idempotents, with $i^2=-1$ carried out in the expansion:

$$
\begin{aligned}
\vec\Upsilon_x\vec\Upsilon_y&=\tfrac14\bigl(i^2\vec e_x^2+i\vec e_x\vec e_y-i\vec e_y\vec e_x-\vec e_y^2\bigr)
=\tfrac14\bigl(e_t+i\vec e_z+i\vec e_z+e_t\bigr)=\tfrac12\bigl(e_t+i\vec e_z\bigr)=\tilde\Pi_+ ,\\
\vec\Upsilon_y\vec\Upsilon_x&=\tfrac12\bigl(e_t-i\vec e_z\bigr)=\tilde\Pi_- .
\end{aligned}
$$

with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_+^{*}=\tilde\Pi_+$ and $\tilde\Pi_++\tilde\Pi_-=e_t$. Summing the two products gives the anticommutator, subtracting them gives the commutator, and each square vanishes:

$$
\boxed{\;\vec\Upsilon_x^2=0 ,
\qquad
\vec\Upsilon_y^2=0 ,
\qquad
\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t ,
\qquad
[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z\;}.
$$

The pair $\vec\Upsilon_x,\vec\Upsilon_y$ therefore satisfies the canonical anticommutation relations, while the commutator, being the difference $\tilde\Pi_+-\tilde\Pi_-$ of the two idempotents, fails the bosonic relation by an element of $\mathbb{M}_+$ rather than by a c-number. The tracelessness of a commutator ($\mathrm{Tr}[\tilde{Q},\tilde Q_1]=0$, while $\mathrm{Tr}\,e_t=2$) shows that no bosonic mode with a central commutator exists here, so the algebra's one mode is fermionic — the algebra's finite content is the fermionic Fock space.

The spin generators are the bilinears

$$
\tilde S_k=\tfrac{\hbar}{2}\,i\vec e_k ,
\qquad
[\tilde S_a,\tilde S_b]=i\hbar\,\epsilon_{abc}\,\tilde S_c ,
\qquad
\tilde S_\pm=\tilde S_x\pm i\tilde S_y ,
$$

$$
\tilde S_+=\tfrac{\hbar}{2}\big(i\vec e_x-\vec e_y\big)=\hbar\,\vec\Upsilon_x ,
\qquad
\tilde S_-=\tfrac{\hbar}{2}\big(i\vec e_x+\vec e_y\big)=\hbar\,\vec\Upsilon_y ,
$$

which the spin-$\tfrac12$ companion derives. Comparing the two displays identifies the one-site spin ladder with the one-site fermionic mode:

$$
\vec\Upsilon_x=\tilde S_+/\hbar ,
\qquad
\vec\Upsilon_y=\tilde S_-/\hbar .
$$

**This is the one-site Jordan–Wigner transformation**, and it is an identity inside $\mathbb{B}$ rather than a transformation. The reason it needs no string is structural: the string is a product of the *other* sites' parities, and at one site there are no other sites. Equivalently, the string is $\prod_{k<j}(-1)^{n_k}$ and the empty product is the identity. The algebra's contribution to the Jordan–Wigner story is therefore not the string but the fact that the transformation has a one-site fixed point: the spin and the fermion are two interpretations of the same biquaternion, the interpretation changing only when a *second* site is present.

### The Two Readings of the Identification

Two readings of the same element are in use in the series, and they differ by a sign carried by right multiplication by $\vec e_z$. Both are stated here, because the one-site map is exact in one and picks up that sign in the other.

The $2\times2$ reading is the complex-linear isomorphism $\mathsf M_2$ of the matrix models, $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$; it is the left action on a Peirce carrier, and it is the one the companion articles use. The cell reading is $\mathbb R$-linear and sends each real unit to a two-sided operator, $e_t\mapsto L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $\vec e_k\mapsto L_{\vec e_k}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and $i\mapsto L_{e_t}^{\mathrm{axf}}R_{e_z}$, with the cells $L_aR_b$ acting by $\psi\mapsto a\psi b$ and multiplying by $L_aR_b\,L_cR_d=L_{ac}R_{db}$. The two readings are

| Element | $2\times2$ image $\mathsf M_2$ | Cell |
|---|---|---|
| $e_t$ | $I_2$ | $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $\vec e_k$ | $-i\sigma_k$ | $L_{\vec e_k}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $i$ | $iI_2$ | $L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=R_{\vec e_z}^{\mathrm{axf}}$ |
| $i\vec e_k$ | $\sigma_k$ | $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $\vec\Upsilon_x$ | $\sigma_+$ | $\tfrac12\bigl(L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}-L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\bigr)$ |
| $\vec\Upsilon_y$ | $\sigma_-$ | $\tfrac12\bigl(L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}+L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\bigr)$ |

A real unit and an imaginary unit are each a single cell, while the ladder is a sum of two, because the reading is $\mathbb R$-linear and not $\mathbb C$-linear. The sign that separates the two readings is carried by right multiplication by $\vec e_z$. That multiplication is a scalar on each Peirce carrier, $\tilde\Pi_+\vec e_z=-i\tilde\Pi_+$ and $\tilde\Pi_-\vec e_z=+i\tilde\Pi_-$, so the cell of $i\vec e_k$ is $-i$ times the left action on the first carrier and $+i$ times the left action on the second. In matched bases — bases of the two carriers that a left-module isomorphism carries into one another, so that the left action is the same matrix $\mathsf M_2$ on both — the cell is

$$
\begin{aligned}
\text{on }\mathbb{B}\tilde\Pi_+:\quad & -i\,\mathsf M_2(\vec e_k)=(-i)(-i)\sigma_k=-\sigma_k ,\\
\text{on }\mathbb{B}\tilde\Pi_-:\quad & +i\,\mathsf M_2(\vec e_k)=(+i)(-i)\sigma_k=+\sigma_k ,
\end{aligned}
$$

both signs using $i^2=-1$. The $2\times2$ image is the left action alone and carries one sign, $\mathsf M_2(i\vec e_k)=\sigma_k$; the cell acts from both sides and carries both.

The two carriers are the algebra's two minimal left ideals, both copies of the spinor module $S$. The sign that separates them is the Peirce sign $P=R_{i\vec e_z}^{\mathrm{axf}}$. Since $R_{i\vec e_z}^{\mathrm{axf}}=iR_{\vec e_z}^{\mathrm{axf}}$, and $R_{\vec e_z}^{\mathrm{axf}}$ is $-i$ on $S_+$ and $+i$ on $S_-$, the Peirce sign is $+1$ on $S_+$ and $-1$ on $S_-$. It is a copy index, not the chirality. The chirality is the cell $\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{axf}}$, a pure right multiplication; its central form is the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra, and on the Dirac module the two agree up to an overall sign. The relation is recorded in *The Legacy Pauli Gamma Formulation* below.

The one-site identification is exact inside the algebra, and its $2\times2$ image is exact as well:

$$
\mathsf M_2(\vec\Upsilon_x)=\sigma_+ ,
\qquad
\mathsf M_2(\vec\Upsilon_y)=\sigma_- ,
\qquad
\mathsf M_2(\vec\Upsilon_y)=\mathsf M_2(\vec\Upsilon_x)^\dagger ,
$$

$$
\mathsf M_2\bigl([\vec\Upsilon_x,\vec\Upsilon_y]\bigr)=\mathsf M_2(i\vec e_z)=\sigma_z ,
\qquad
\{\mathsf M_2(\vec\Upsilon_x),\mathsf M_2(\vec\Upsilon_y)\}=I_2 .
$$

All five were checked by exact matrix multiplication, together with $\mathsf M_2(\vec e_x\vec e_y)=\mathsf M_2(\vec e_z)$. The one-site identification above is the $N=1$ case of the chain map, and the chain map is the subject of the rest of the article.

## The Many-Site Map

Let the chain carry $N$ spins, with Hilbert space $\mathcal{H}=\bigotimes_{j=1}^N\mathbb{C}^2$ and Pauli operators $(\sigma_\alpha)_{j}$ acting on site $j$. Define the fermionic modes by the Jordan–Wigner prescription in the convention above,

$$
c^{\mathrm{fop}}_j=\Big(\prod_{k=1}^{j-1}(\sigma_z)_{k}\Big)(\sigma_+)_{j} ,
\qquad
c^{\mathrm{fop}\dagger}_j=\Big(\prod_{k=1}^{j-1}(\sigma_z)_{k}\Big)(\sigma_-)_{j} .
$$

The string $\prod_{k<j}(\sigma_z)_{k}$ is Hermitian and $*$-unitary, and it commutes with $(\sigma_\pm)_{j}$ because it acts on different sites. Three identities follow, and all three were verified by exact matrix computation on chains of up to four sites with the Kronecker-product representation of $\mathcal{H}$.

**The anticommutator.** For $i,j$ in any order,

$$
\boxed{\;\{c^{\mathrm{fop}}_i,c^{\mathrm{fop}}_j\}=0 ,
\qquad
\{c^{\mathrm{fop}}_i,c^{\mathrm{fop}\dagger}_j\}=\delta_{ij}\,I\;}.
$$

The verification on $N=4$ returned a maximum error of exactly $0$ over all $16$ pairs and all $256$ matrix entries. The cancellation of the string requires that the two sites be ordered. For $i<j$ the string of $c^{\mathrm{fop}}_j$ carries the parity of every site up to $j$, and the only factor that meets a raising operator is $(\sigma_z)_{i}$: in $S_j(\sigma_+)_{j}S_i(\sigma_+)_{i}$ it sits immediately to the right of $(\sigma_+)_{i}$, and $\sigma_+\sigma_z=-\sigma_+$ is the whole sign. The factors with $i<k<j$ commute with $(\sigma_+)_{i}$ and cost nothing, which is why the string cancels for every pair of sites and not only for adjacent ones.

**The number and the parity.** With the sign convention stated,

$$
n_j=c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_j=\frac{I-(\sigma_z)_{j}}{2} ,
\qquad
(-1)^{n_j}=(\sigma_z)_{j} ,
$$

so the occupied state is the spin-down state and the fermionic parity of a site *is* the site's $(\sigma_z)_{j}$. The first identity was checked term by term, the second follows from it in the two-dimensional site space and was checked as a matrix identity on the full chain.

**The hopping and the inverse.** The quadratic fermions reproduce the XY coupling,

$$
c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_{j+1}+c^{\mathrm{fop}\dagger}_{j+1}c^{\mathrm{fop}}_j
=\tfrac12\big((\sigma_x)_{j}(\sigma_x)_{j+1}+(\sigma_y)_{j}(\sigma_y)_{j+1}\big) ,
$$

and the inverse map returns the transverse spin components,

$$
(\sigma_x)_{j}=\Big(\prod_{k<j}(\sigma_z)_{k}\Big)\big(c^{\mathrm{fop}}_j+c^{\mathrm{fop}\dagger}_j\big) ,
\qquad
(\sigma_z)_{j}=I-2 n_j .
$$

Both were verified bond by bond and site by site on the four-site chain, with maximum errors of $0$. The inverse displays the asymmetry of the transformation: recovering a spin operator requires the same string that the fermion carried, so the map is an isomorphism of algebras but the *fermion* mode is defined only relative to an ordering of the sites.

### The String Is a Product of One-Site Parities

The string is not a novel object. Using the parity identity above,

$$
\prod_{k<j}(\sigma_z)_{k}=\prod_{k<j}(-1)^{F_k} ,
\qquad F_k=n_k ,
$$

where the one-site factor is the algebra element the parents identify in the one-mode case,

$$
(-1)^{F}=i\vec e_z=2\tilde S_z/\hbar ,
$$

that is, $(-1)^{F_k}$ read inside $\mathbb{B}$.

The Jordan–Wigner string is therefore the tensor product of the one-site biquaternion parities,

$$
\prod_{k<j}(-1)^{F_k}\;\in\;\bigotimes_{k=1}^{j-1}\mathbb{B} ,
$$

one factor of $i\vec e_z$ per site to the left. This is the biquaternion content of the transformation, and it explains both of its structural features at once.

- **Why one site needs no string.** The empty product of one-site parities is the identity, and the one-site map is the algebra's identity of the previous section.
- **Why the string is not in $\mathbb{B}$.** For $N\ge2$ the string is a tensor product with at least one nontrivial factor, so it lies outside the diagonal copy of $\mathbb{B}$ in $\bigotimes\mathbb{B}$; the algebra has no way to express a parity of *another* site. The grading that the spin–statistics companion records as external for the field is, for the chain, exactly the string.

## The Map as an Algebra Isomorphism and Its Grading

The Jordan–Wigner map has a sharp algebraic description that the biquaternion framework makes transparent.

**Both algebras are the full matrix algebra.** The spin operators $(\sigma_\alpha)_{j}$ generate $\bigotimes_j M_2(\mathbb{C})=M_{2^N}(\mathbb{C})$; the fermionic modes $c^{\mathrm{fop}}_j,c^{\mathrm{fop}\dagger}_j$ generate the same matrix algebra, since $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$, verified by rank computation for $N=1$ ($\dim 4$) and $N=2$ ($\dim 16$). The Jordan–Wigner map is the explicit isomorphism between these two presentations of the same algebra, and it is unital.

**It preserves the parity grading and it does not preserve locality.** The two transverse spins are odd in the modes and the longitudinal one is even,

$$
(\sigma_x)_{j}=\Big(\prod_{k<j}(\sigma_z)_{k}\Big)\big(c^{\mathrm{fop}}_j+c^{\mathrm{fop}\dagger}_j\big) ,
\qquad
(\sigma_y)_{j}=-i\Big(\prod_{k<j}(\sigma_z)_{k}\Big)\big(c^{\mathrm{fop}}_j-c^{\mathrm{fop}\dagger}_j\big) ,
$$

$$
(\sigma_z)_{j}=I-2c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_j ,
$$

so a one-site spin operator is not a one-site fermion operator of definite degree: the transverse components carry the whole string to the left of the site. The parity operator is the same operator on the two sides, $(-1)^{F}=\prod_j(\sigma_z)_{j}=\prod_j(I-2c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_j)$; it commutes with $(\sigma_z)_{j}$ and anticommutes with $(\sigma_x)_{j}$ and $(\sigma_y)_{j}$, so the map **does** respect the parity grading. What it does not respect is the site structure: locality is lost in both directions, since $c^{\mathrm{fop}}_j$ is a string times $(\sigma_+)_{j}$ and $(\sigma_x)_{j}$ is a string times $c^{\mathrm{fop}}_j+c^{\mathrm{fop}\dagger}_j$.

**The transformation is a square root.** The mode algebra is graded by the parity, $\mathcal{A}=\mathcal{A}_{\mathrm{even}}\oplus\mathcal{A}_{\mathrm{odd}}$, and the even part is spanned by the products of an even number of odd elements; it is generated by the number bilinears $c^{\mathrm{fop}\dagger}_ic^{\mathrm{fop}}_j$ together with the pairing bilinears $c^{\mathrm{fop}}_ic^{\mathrm{fop}}_j$ and $c^{\mathrm{fop}\dagger}_ic^{\mathrm{fop}\dagger}_j$. The number bilinears alone do not suffice: at $N=2$ they generate an algebra of dimension $6$, while the even part has dimension $8$. Passing from spins to fermions is taking a square root of the observable algebra — the modes are the odd generators, and their products span the even part — and the string is the choice of branch. In biquaternion language the one-site even part is the span of $e_t$ and the parity $i\vec e_z$, that is $\mathbb{C}\oplus\mathbb{C}$ with idempotents $(e_t\pm i\vec e_z)/2$, and the modes are the odd elements adjoined to it — the same structure that the parent Fock-space article exhibits for one mode, here extended over sites by the parity product. This is also why the map cannot be canonical: a square root has a branch, and the branch is the string's ordering.

## Consequences for the Chain

**Free fermions.** The hopping identity converts the XY Hamiltonian into a quadratic fermionic form. The spin form is

$$
\boxed{\;H_{XY}=-J\sum_j\Big((\sigma_x)_{j}(\sigma_x)_{j+1}+(\sigma_y)_{j}(\sigma_y)_{j+1}\Big)\;}
$$

and the fermion form, equal to it term by term through the hopping identity, is

$$
H_{XY}=-2J\sum_j\Big(c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_{j+1}+c^{\mathrm{fop}\dagger}_{j+1}c^{\mathrm{fop}}_j\Big) ,
$$

which is a free-fermion Hamiltonian, diagonalised by a Bogoliubov transformation in momentum space. The transverse-field Ising chain is brought to the same free-fermion form up to a pairing term $c^{\mathrm{fop}}_jc^{\mathrm{fop}}_{j+1}+c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}\dagger}_{j+1}$, which a Majorana decomposition absorbs. The transcription is standard and is recorded as such; the biquaternion framework adds nothing to the solution.

**A two-site example.** For $N=2$ the identity can be exhibited in full. In the ordered basis $\{|\!\uparrow\uparrow\rangle,|\!\uparrow\downarrow\rangle,|\!\downarrow\uparrow\rangle,|\!\downarrow\downarrow\rangle\}$ of $\mathbb{C}^2\otimes\mathbb{C}^2$, the spin and fermion forms of the XY Hamiltonian agree exactly,

$$
-J\big((\sigma_x)_{1}(\sigma_x)_{2}+(\sigma_y)_{1}(\sigma_y)_{2}\big)
=-2J\big(c^{\mathrm{fop}\dagger}_1c^{\mathrm{fop}}_2+c^{\mathrm{fop}\dagger}_2c^{\mathrm{fop}}_1\big),
\qquad
\max|H_{\text{spin}}-H_{\text{ferm}}|=0 ,
$$

and both have the spectrum $\{-2J,0,0,+2J\}$ — a non-degenerate ground state, a non-degenerate excited state, and a doubly degenerate level at zero, which is the free-fermion spectrum of two modes with the hopping turned on. The whole-chain parity $(-1)^{F}=(\sigma_z)_{1}(\sigma_z)_{2}$ commutes with the Hamiltonian, with commutator norm exactly $0$, so the two sectors are separately diagonalised. The whole zero level lies in the even sector — its two states are the empty state and the doubly occupied one — while the two odd states are the split pair at $\mp2J$. The degeneracy at zero is therefore the particle–hole pairing of the free theory and not a parity degeneracy: the whole-chain parity does not resolve it.

### The String as a Cocycle

The string has one more structural property that the spin language hides and the fermion language makes plain: it is a multiplicative one-cocycle of the site ordering. Writing $S_j=\prod_{k<j}(\sigma_z)_{k}$ for the string, the increment from one site to the next is that site's own parity,

$$
S_{j+1}=S_j(\sigma_z)_{j} ,
\qquad
S_jS_i^{-1}=\prod_{i\le k<j}(\sigma_z)_{k}\quad(i<j),
$$

so the relative string of two sites is the parity of the interval between them. Three things follow. The modes anticommute, $c^{\mathrm{fop}}_ic^{\mathrm{fop}}_j=-c^{\mathrm{fop}}_jc^{\mathrm{fop}}_i$ for $i\ne j$, and the sign is the single factor $(\sigma_z)_{i}$ that the longer string carries before $(\sigma_+)_{i}$. Each mode is defined only relative to the ordering, since $c^{\mathrm{fop}}_j$ carries the parity of every site to its left. And the transformation is nonlocal for a reason the cochain makes visible: an operator supported on one site of the spin chain is supported on that site and on every site to its left in the fermion chain.

The biquaternion interpretation is the same as before: the increments of the cochain are the one-site parities $(-1)^{F_k}=i\vec e_z$, so the relative string of two sites is the tensor product of that many factors of the algebra's parity, and the cocycle condition is the statement that these products multiply consistently.

**The boundary term.** The string makes the map nonlocal, and the nonlocality has a physical place: it sits at the chain's ends. The fermion-parity operator of the whole chain,

$$
(-1)^{F}=\prod_j(\sigma_z)_{j} ,
$$

is the product of the on-site parities and commutes with $H_{XY}$; the two sectors it labels carry different boundary conditions for the fermions. In the ordered phase of the transverse-field Ising chain the two lowest states of the two sectors are nearly degenerate, and that near-degeneracy is the standard signature of the $\mathbb{Z}_2$ symmetry in the spin language and of the two boundary-condition sectors in the fermion language.

**The hidden symmetry.** The map also shows why an operator that is simple in one language need not be simple in the other: the parity is the product of on-site spins, $\prod_j(\sigma_z)_{j}$, and the modes contribute the diagonal operator $(-1)^{\hat N}$ with $\hat N=\sum_j c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_j$, while the hopping is a two-site spin operator and a bilinear in the modes. The transformation does not create or destroy symmetry; it relabels which generators are simple.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The Jordan–Wigner transformation itself, the string, the anticommutators, the number and parity identities, the hopping identity, the inverse map, the free-fermion solution of the XY and transverse-field Ising chains, and the boundary-condition sectors. This is textbook material in the stated convention, and every sign was recomputed on chains up to $N=4$.

**The algebra's own.**

- *The one-site identity.* The parents' $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ is the one-site Jordan–Wigner map, an identity inside $\mathbb{B}$; the transformation has a one-site fixed point.
- *The string as the product of one-site parities.* $\prod_{k<j}(\sigma_z)_{k}=\prod_{k<j}(-1)^{F_k}$, with $(-1)^F=i\vec e_z$ the parent's algebra element. The string is the tensor product of the algebra's parities, and its non-diagonality is the external grading the spin–statistics companion records.
- *The grading statement.* The parity is available on both sides, $(-1)^{F}=\prod_j(\sigma_z)_{j}$, and the map respects it: $(\sigma_z)_{j}$ is even, the transverse spins are odd, the modes are odd. What the map does not preserve is the site structure, since a one-site spin operator becomes a string-laden fermion operator.
- *The two readings.* The $2\times2$ image is one-sided and carries one sign, $\mathsf M_2(i\vec e_k)=\sigma_k$, while the cell $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ acts on the two Peirce carriers with opposite signs, $-\sigma_k$ on one and $+\sigma_k$ on the other. The difference is right multiplication by $i\vec e_z$, the Peirce copy index; the chirality is the cell $\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{axf}}$, and the two agree on the Dirac module up to an overall sign.

**Open.**

- **The chain and the field.** The chain's isomorphism is between finite-dimensional algebras; the field's grading remains external, as the spin–statistics companion records, and no continuum version of the string is adopted here.
- **Boundary conditions in the continuum.** The relation between the chain's two parity sectors and the field's boundary conditions is standard for the lattice and is not pushed to the continuum here.
- **The uniqueness of the square root.** The Jordan–Wigner map is one choice of square root of the observable algebra; whether the algebra singles out a preferred ordering, and hence a preferred string, is not determined by anything used here.

## Companion Articles

- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder identified here with the one-site spin, and the parity $(-1)^F=i\vec e_z$.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the identification $i\vec e_k\mapsto L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and the $2\times2$ image $\mathsf M_2$ that fixes the one-site map.
- Companion article *Biquaternion Physical Interpretation of Operator Chirality*, for the definition of chirality as the side on which an operator multiplies, the identification of $\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}$ as a pure right multiplier, and the coincidence $P=-\gamma_5[\mathbb{M}_-]$ for the aligned root.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are cells of the same two-sided operator algebra that the one-site identification used, and the chirality cell is the right multiplication by $\vec e_z$ that separated the two carriers there.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

The four frame cells are the four coordinates, with the factor $i$ belonging to the cell:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$

The fifth gamma is not a fifth frame vector but their product, and $i^2=-1$ fixes its sign and its cell. Multiplying cells, $L_aR_b\,L_cR_d=L_{ac}R_{db}$, with $\vec e_x\vec e_x=\vec e_y\vec e_y=-e_t$ and $\vec e_x\vec e_y=-\vec e_y\vec e_x=\vec e_z$,

$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},
\qquad
\gamma_5[\mathbb{M}_-]:=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=i\bigl(-L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\bigr)=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=-iR_{\vec e_z}^{\mathrm{pau}}.
$$

In the axis-free display:

$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
\qquad
\gamma_5[\mathbb{M}_-]:=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=i\bigl(-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\bigr)=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}.
$$

The four gammas carry $i^4=1$, so the single $i$ of the definition survives, and no second factor of $i$ is left over: the cell that results is $-iR_{\vec e_z}^{\mathrm{pau}}$, in which the left multiplier is the identity and the cell has collapsed to a right multiplication.

That right multiplication is the one the one-site section met, up to the factor $i$: the Peirce sign of the two carriers is $P=R_{i\vec e_z}^{\mathrm{pau}}=iR_{\vec e_z}^{\mathrm{pau}}$, so

$$
\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{pau}}=-P ,
\qquad
P^2=I_4 ,
$$

The same identities in the axis-free display:

$$
\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{axf}}=-P ,
\qquad
P^2=I_4 ,
$$

and the two differ only by the overall sign that the frame fixes. The Peirce sign is a copy index inside $\mathbb{B}$; the chirality is not. The chirality is the cell $\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{axf}}$, whose central form is the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra.

The frame is Clifford, with $\varepsilon=(1,-1,-1,-1)$ and $I_4=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ the identity cell:

$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4 ,
\qquad
\gamma_5[\mathbb{M}_-]^2=I_4 ,
\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0 ,
\qquad \varepsilon=(1,-1,-1,-1),$$

all three checked cell by cell.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality $\Gamma$. The central grading is a different object and carries its own factors: $\tilde\Xi_{\mathrm{ad}}$ is the central root of the double with $\tilde\Xi_{\mathrm{ad}}^2=-e_t$, so $\chi=i\tilde\Xi_{\mathrm{ad}}$ has

$$
\chi^2=i^2\tilde\Xi_{\mathrm{ad}}^2=(-1)(-e_t)=e_t ,
$$

and $\chi$ is the difference of the two central idempotents of the complexified algebra, $(e_t+\chi)/2-(e_t-\chi)/2=\chi$. The cell represents $\chi$ on the Dirac module; it is not its definition. The chirality pairs the two halves of that module, and the field article writes the pair as two equations, one for each chirality:

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L ,
$$

$$
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R .
$$

The two act from the left; what separates them is the conjugation $\natural$, not a change of side. The mass is the one term of the pair that mixes the two chiralities.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Jordan–Wigner transformation in biquaternion form has a one-site fixed point inside the algebra and is extended over sites by the product of the algebra's parities. At one site the parents' ladder $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ satisfies $\vec\Upsilon_x^2=0$, $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, $[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z$, and its two products are the Peirce idempotents $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$, so a one-site spin ladder *is* a fermionic mode and the string is the empty product.

For $N$ sites, with $c^{\mathrm{fop}}_j=(\prod_{k<j}(\sigma_z)_{k})(\sigma_+)_{j}$ and the spin-down state occupied,

$$
\{c^{\mathrm{fop}}_i,c^{\mathrm{fop}\dagger}_j\}=\delta_{ij} ,
\qquad
n_j=\frac{I-(\sigma_z)_{j}}{2} ,
\qquad
(-1)^{n_j}=(\sigma_z)_{j} ,
$$

$$
c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_{j+1}+\text{h.c.}
=\tfrac12\big((\sigma_x)_{j}(\sigma_x)_{j+1}+(\sigma_y)_{j}(\sigma_y)_{j+1}\big),
$$

all four verified with zero error on chains of up to four sites. The string is the product of one-site parities, $\prod_{k<j}(\sigma_z)_{k}=\prod_{k<j}(-1)^{F_k}$, each factor being the parent's $(-1)^F=i\vec e_z$; it is trivial at one site and non-diagonal beyond, which is the same externality of the grading that the spin–statistics companion records for the field.

The map is a unital algebra isomorphism — both presentations generate $M_{2^N}(\mathbb{C})$, verified by rank computation for $N=1,2$ — it preserves the parity grading, and it is not local: a one-site spin operator becomes a string-laden fermion operator, the modes are the odd generators whose products span the even part, and the string is the choice of branch. The consequences are the standard ones: the XY chain becomes free fermions, the whole-chain parity $\prod_j(\sigma_z)_{j}$ labels the two boundary-condition sectors, and the near-degeneracy of the ordered phase appears as the standard $\mathbb{Z}_2$ structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | One-site fermionic mode inside $\mathbb{B}$ |
| $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, $[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z$ | CAR inside the algebra; commutator not central |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | Peirce idempotents, $\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y$ and $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x$ |
| $\mathsf M_2(\vec e_k)=-i\sigma_k$, $\mathsf M_2(i\vec e_k)=\sigma_k$ | Complex-linear $2\times2$ image of the algebra |
| $L_aR_b$, $L_aR_b\,L_cR_d=L_{ac}R_{db}$ | The two-sided cell, $\psi\mapsto a\psi b$ |
| $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, $\tilde S_+=\hbar\,\vec\Upsilon_x$, $\tilde S_-=\hbar\,\vec\Upsilon_y$ | Spin generators; one-site JW identity $\vec\Upsilon_x=\tilde S_+/\hbar$ |
| $(\sigma_\alpha)_{j}$, $(\sigma_\pm)_{j}=\tfrac12((\sigma_x)_{j}\pm i(\sigma_y)_{j})$ | Pauli operator on site $j$; the outer subscript is a site label, not a tensor index |
| $c^{\mathrm{fop}}_j=(\prod_{k<j}(\sigma_z)_{k})(\sigma_+)_{j}$ | Jordan–Wigner fermion (spin-down occupied) |
| $\prod_{k<j}(\sigma_z)_{k}=\prod_{k<j}(-1)^{F_k}$ | The string as a product of one-site parities |
| $(-1)^{F}=i\vec e_z=2\tilde S_z/\hbar$ | One-site parity, the string's factor |
| $\{c^{\mathrm{fop}}_i,c^{\mathrm{fop}\dagger}_j\}=\delta_{ij}$, $\{c^{\mathrm{fop}}_i,c^{\mathrm{fop}}_j\}=0$ | Canonical anticommutators (verified, error $0$) |
| $n_j=(I-(\sigma_z)_{j})/2$, $(-1)^{n_j}=(\sigma_z)_{j}$ | Number and parity |
| $c^{\mathrm{fop}\dagger}_jc^{\mathrm{fop}}_{j+1}+\text{h.c.}=\tfrac12((\sigma_x)_{j}(\sigma_x)_{j+1}+(\sigma_y)_{j}(\sigma_y)_{j+1})$ | Hopping = XY bond |
| $(\sigma_x)_{j}=(\prod_{k<j}(\sigma_z)_{k})(c^{\mathrm{fop}}_j+c^{\mathrm{fop}\dagger}_j)$ | Inverse map |
| $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$ | Both descriptions generate the full matrix algebra |
| $(-1)^{F}=\prod_j(\sigma_z)_{j}$ | Whole-chain parity; boundary-condition sectors |
| $i\vec e_k\mapsto L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Cell of the timelike bivector $i\vec e_k$; it acts as $-\sigma_k$ on $\mathbb{B}\tilde\Pi_+$ and $+\sigma_k$ on $\mathbb{B}\tilde\Pi_-$ |
| $P=R_{i\vec e_z}^{\mathrm{axf}}$ | Peirce sign of the two carriers, $+1$ on $S_+$ and $-1$ on $S_-$; a copy index, not the chirality |

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
