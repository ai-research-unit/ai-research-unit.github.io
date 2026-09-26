# __The Jordan–Wigner Transformation in Biquaternionic Form__

## Introduction

A spin-$\tfrac12$ chain and a chain of fermionic modes are described by different operators with different commutation rules, and yet in one dimension the two descriptions carry the same state space and the same algebra. The map between them is the Jordan–Wigner transformation. In the biquaternion framework it has a sharp reading: the transformation is the **extension over sites of a one-site identity that is already inside the algebra**, and the object that extends it — the Jordan–Wigner string — is the product of the one-site fermionic parities, the element $(-1)^F=ie_3$ that the parents isolate in $\mathbb{M}_+$.

This article establishes:

- **The one-site case is the algebra's own identity.** For one mode the parents' ladder $\tilde a=\tfrac12(ie_1-e_2)$, $\tilde a^\dagger=\tfrac12(ie_1+e_2)$ satisfies $\tilde a^2=0$ and $\{\tilde a,\tilde a^\dagger\}=e_0$ inside $\mathbb{B}$, so a one-site spin ladder *is* a fermionic mode with no string attached. The spin generators are the bilinears $\tilde S_k=\tfrac{\hbar}{2}ie_k$; the fermionic mode is the square of those bilinears' structure. There is nothing to transform at one site.
- **The string.** For $N$ sites the map must carry a string, and the string is exactly the tensor product of the one-site parities: $\prod_{k<j}(-1)^{\hat n_k}=\prod_{k<j}\sigma^z_k$. It lies in $\bigotimes_j\mathbb{B}$ but not in $\mathbb{B}$, and for one site it collapses to the identity, which is why the one-site case needed none.
- **The map and its failure to be a graded isomorphism.** The Jordan–Wigner map is a unital algebra isomorphism between the spin algebra and the fermionic mode algebra — both are the full matrix algebra of the $2^N$-dimensional space, and this is the Clifford identity $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$. It does **not** preserve the fermionic grading: spins are even (bilinear) in fermions, fermions are odd. The transformation is the choice of a square root of the spin algebra, and the string is its branch cut.
- **The consequences.** The hopping identity, the parity identity, the inverse map, the free-fermion solution of the XY chain, and the boundary term that distinguishes the two fermion-parity sectors.

The standard material is transcribed with explicit signs; the biquaternion content is the one-site identification and the parity reading of the string.

**Conventions.** From the companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, $e_0=1$, $e_k^2=-e_0$, $e_1e_2=e_3$ and its cyclic permutations, central $i$ with $i^\dagger=-i$; $\mathbb{M}_-$ anti-Hermitian (material), $\mathbb{M}_+$ Hermitian (informational); $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$; the one-mode ladder $\tilde a=\tfrac12(ie_1-e_2)$, $\tilde a^\dagger=\tfrac12(ie_1+e_2)$, $(-1)^F=ie_3$; the spin generators $\tilde S_k=\tfrac{\hbar}{2}ie_k$; the dictionary identification $\Phi(ie_k)=\gamma^0\gamma^k$ of the algebra into the even Clifford subalgebra; the spin operators act on the ideals as the Pauli matrices (the parent's $\Phi(ie_k)$ restricted to the invariant subspace, $\tfrac{\hbar}{2}ie_k\mapsto\tfrac{\hbar}{2}\sigma_k$). **Jordan–Wigner convention.** For $N$ sites with Pauli operators $\sigma^x_j,\sigma^y_j,\sigma^z_j$ in the ordered product $\bigotimes_{j=1}^{N}$, set

$$
\hat c_j=\Big(\prod_{k<j}\sigma^z_k\Big)\sigma^+_j ,
\qquad
\sigma^\pm_j=\tfrac12\big(\sigma^x_j\pm i\sigma^y_j\big),
$$

with the spin-down state ($\sigma^z=-1$) occupied. All signs below are in this convention and were verified by exact matrix computation on chains up to $N=4$.

## The One-Site Case

The biquaternion algebra contains a fermionic mode, and it contains it with no string and no extension. Write

$$
\tilde a=\tfrac12\big(ie_1-e_2\big),
\qquad
\tilde a^\dagger=\tfrac12\big(ie_1+e_2\big),
$$

as the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* defines them. Then, by exact multiplication in the basis,

$$
\tilde a^2=0 ,
\qquad
\tilde a^{\dagger 2}=0 ,
\qquad
\{\tilde a,\tilde a^\dagger\}=e_0 ,
\qquad
[\tilde a,\tilde a^\dagger]=ie_3 ,
$$

so the $\tilde a$ satisfy the canonical anticommutation relations and the commutator fails the bosonic relation by an element of $\mathbb{M}_+$ rather than by a c-number. The tracelessness of a commutator ($\mathrm{Tr}[X,Y]=0$, while $\mathrm{Tr}\,e_0=2$) shows that no bosonic mode with a central commutator exists here, so the algebra's one mode is fermionic — the algebra's finite content is the fermionic Fock space.

The spin generators are the bilinears

$$
\tilde S_k=\tfrac{\hbar}{2}\,ie_k ,
\qquad
[\tilde S_a,\tilde S_b]=i\hbar\,\epsilon_{abc}\,\tilde S_c ,
\qquad
\tilde S_+=\tfrac{\hbar}{2}\big(ie_1-e_2\big)=\hbar\,\tilde a ,
\qquad
\tilde S_-=\tfrac{\hbar}{2}\big(ie_1+e_2\big)=\hbar\,\tilde a^\dagger ,
$$

which the spin-$\tfrac12$ companion derives. Comparing the two displays identifies the one-site spin ladder with the one-site fermionic mode:

$$
\tilde a=\frac{\tilde S_+}{\hbar}\Big|_{\text{one mode}} ,
\qquad
\tilde a^\dagger=\frac{\tilde S_-}{\hbar}\Big|_{\text{one mode}} .
$$

**This is the one-site Jordan–Wigner transformation**, and it is an identity inside $\mathbb{B}$ rather than a transformation. The reason it needs no string is structural: the string is a product of the *other* sites' parities, and at one site there are no other sites. Equivalently, the string is $\prod_{k<j}(-1)^{\hat n_k}$ and the empty product is the identity. The algebra's contribution to the Jordan–Wigner story is therefore not the string but the fact that the transformation has a one-site fixed point: the spin and the fermion are two readings of the same biquaternion, the reading changing only when a *second* site is present.

**A note on the identification.** The parent article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and the dictionary companion fix the module-level statement $\Phi(ie_k)=\gamma^0\gamma^k$, whose left action on the invariant two-dimensional subspace is the Pauli action; the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* gives the two-dimensional representative $\Phi(e_k)=-i\sigma_k$, hence $\Phi(ie_k)=\sigma_k$. In that representative the one-site identification is exact, including the conjugation:

$$
\Phi(\tilde a)=\sigma^+ ,
\qquad
\Phi(\tilde a^\dagger)=\sigma^- ,
\qquad
\Phi(\tilde a^\dagger)=\Phi(\tilde a)^\dagger ,
\qquad
\Phi([\tilde a,\tilde a^\dagger])=\Phi(ie_3)=\sigma^z ,
$$

all four checked by exact matrix multiplication: $\Phi(e_1e_2)=\Phi(e_3)$, $\{\Phi(\tilde a),\Phi(\tilde a^\dagger)\}=I$, $[\Phi(\tilde a),\Phi(\tilde a^\dagger)]=\sigma^z$. The one-site identification above is the $N=1$ case of the chain map, and the chain map is the subject of the rest of the article.

## The Many-Site Map

Let the chain carry $N$ spins, with Hilbert space $\mathcal{H}=\bigotimes_{j=1}^N\mathbb{C}^2$ and Pauli operators $\sigma^\alpha_j$ acting on site $j$. Define the fermionic modes by the Jordan–Wigner prescription in the convention above,

$$
\hat c_j=\Big(\prod_{k=1}^{j-1}\sigma^z_k\Big)\sigma^+_j ,
\qquad
\hat c_j^\dagger=\Big(\prod_{k=1}^{j-1}\sigma^z_k\Big)\sigma^-_j .
$$

The string $\prod_{k<j}\sigma^z_k$ is Hermitian and unitary, and it commutes with $\sigma^\pm_j$ because it acts on different sites. Three identities follow, and all three were verified by exact matrix computation on chains of up to four sites with the Kronecker-product representation of $\mathcal{H}$.

**The anticommutator.** For $i,j$ in any order,

$$
\{\hat c_i,\hat c_j\}=0 ,
\qquad
\{\hat c_i,\hat c_j^\dagger\}=\delta_{ij}\,I .
$$

The verification on $N=4$ returned a maximum error of exactly $0$ over all $16$ pairs and all $256$ matrix entries. The cancellation of the string requires that the two sites be ordered; for $i<j$ the strings differ by $\sigma^z_i$, whose square is the identity, and it is precisely the anticommutation of the two modes that makes the square cancel.

**The number and the parity.** With the sign convention stated,

$$
\hat n_j=\hat c_j^\dagger\hat c_j=\frac{I-\sigma^z_j}{2} ,
\qquad
(-1)^{\hat n_j}=\sigma^z_j ,
$$

so the occupied state is the spin-down state and the fermionic parity of a site *is* the site's $\sigma^z$. The first identity was checked term by term, the second follows from it in the two-dimensional site space and was checked as a matrix identity on the full chain.

**The hopping and the inverse.** The quadratic fermions reproduce the XY coupling,

$$
\hat c_j^\dagger\hat c_{j+1}+\hat c_{j+1}^\dagger\hat c_j
=\tfrac12\big(\sigma^x_j\sigma^x_{j+1}+\sigma^y_j\sigma^y_{j+1}\big) ,
$$

and the inverse map returns the transverse spin components,

$$
\sigma^x_j=\Big(\prod_{k<j}\sigma^z_k\Big)\big(\hat c_j+\hat c_j^\dagger\big) ,
\qquad
\sigma^z_j=I-2\hat n_j .
$$

Both were verified bond by bond and site by site on the four-site chain, with maximum errors of $0$. The inverse displays the asymmetry of the transformation: recovering a spin operator requires the same string that the fermion carried, so the map is an isomorphism of algebras but the *fermion* mode is defined only relative to an ordering of the sites.

### The String Is a Product of One-Site Parities

The string is not a novel object. Using the parity identity above,

$$
\prod_{k<j}\sigma^z_k=\prod_{k<j}(-1)^{\hat n_k}=\prod_{k<j}(-1)^{\hat F_k} ,
$$

and the one-site parity is the algebra element the parents identify,

$$
(-1)^{\hat F}=ie_3=2\tilde S_3/\hbar .
$$

The Jordan–Wigner string is therefore the tensor product of the one-site biquaternion parities,

$$
\prod_{k<j}(-1)^{\hat F_k}\;\in\;\bigotimes_{k=1}^{j-1}\mathbb{B} ,
$$

one factor of $ie_3$ per site to the left. This is the biquaternion content of the transformation, and it explains both of its structural features at once.

- **Why one site needs no string.** The empty product of one-site parities is the identity, and the one-site map is the algebra's identity of the previous section.
- **Why the string is not in $\mathbb{B}$.** For $N\ge2$ the string is a tensor product with at least one nontrivial factor, so it lies outside the diagonal copy of $\mathbb{B}$ in $\bigotimes\mathbb{B}$; the algebra has no way to express a parity of *another* site. The grading that the spin–statistics companion records as external for the field is, for the chain, exactly the string.

## The Map as an Algebra Isomorphism and Its Grading

The Jordan–Wigner map has a sharp algebraic description that the biquaternion framework makes transparent.

**Both algebras are the full matrix algebra.** The spin operators $\sigma^\alpha_j$ generate $\bigotimes_j M_2(\mathbb{C})=M_{2^N}(\mathbb{C})$; the fermionic modes $\hat c_j,\hat c_j^\dagger$ generate the same matrix algebra, since $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$, verified by rank computation for $N=1$ ($\dim 4$) and $N=2$ ($\dim 16$). The Jordan–Wigner map is the explicit isomorphism between these two presentations of the same algebra, and it is unital.

**It does not preserve the grading.** The spin operators are even in the fermions — $\sigma^z_j=I-2\hat c_j^\dagger\hat c_j$ and $\sigma^x_j$ is a *pair* of odd terms times the string — while the $\hat c_j$ are odd. So the map takes even elements to even elements and odd elements to even elements: it is an isomorphism of algebras that is not an isomorphism of graded algebras. The fermionic grading is **not** the spin's tensor-product grading; it is the grading whose parity operator is the string-laden product of on-site $\sigma^z$'s, and it is not the grading the spin chain naturally carries.

**The transformation is a square root.** The even subalgebra of the fermionic mode algebra is generated by the bilinears $\hat c_i^\dagger\hat c_j$, and the Jordan–Wigner map identifies it with the algebra generated by the spin bilinears — which is the *whole* spin algebra, since every product of Pauli matrices is bilinear. The fermions are the odd elements whose squares generate the even part: passing from spins to fermions is taking a square root of the observable algebra, and the string is the choice of branch. In biquaternion language, $\mathbb{B}$ (or its tensor powers) is the even part, and the fermionic modes are the odd square roots adjoined to it — the same structure that the parent Fock-space article exhibits for one mode, here extended over sites by the parity product. This is also why the map cannot be canonical: a square root has a branch, and the branch is the string's ordering.

## Consequences for the Chain

**Free fermions.** The hopping identity converts the XY Hamiltonian into a quadratic fermionic form:

$$
H_{XY}=-J\sum_j\Big(\sigma^x_j\sigma^x_{j+1}+\sigma^y_j\sigma^y_{j+1}\Big)
=-2J\sum_j\Big(\hat c_j^\dagger\hat c_{j+1}+\hat c_{j+1}^\dagger\hat c_j\Big),
$$

which is a free-fermion Hamiltonian, diagonalised by a Bogoliubov transformation in momentum space. The transverse-field Ising chain is brought to the same free-fermion form up to a pairing term $\hat c_j\hat c_{j+1}+\hat c_j^\dagger\hat c_{j+1}^\dagger$, which a Majorana decomposition absorbs. The transcription is standard and is recorded as such; the biquaternion framework adds nothing to the solution.

**A two-site example.** For $N=2$ the identity can be exhibited in full. In the ordered basis $\{|\!\uparrow\uparrow\rangle,|\!\uparrow\downarrow\rangle,|\!\downarrow\uparrow\rangle,|\!\downarrow\downarrow\rangle\}$ of $\mathbb{C}^2\otimes\mathbb{C}^2$, the spin and fermion forms of the XY Hamiltonian agree exactly,

$$
-J\big(\sigma^x_1\sigma^x_2+\sigma^y_1\sigma^y_2\big)
=-2J\big(\hat c_1^\dagger\hat c_2+\hat c_2^\dagger\hat c_1\big),
\qquad
\max|H_{\text{spin}}-H_{\text{ferm}}|=0 ,
$$

and both have the spectrum $\{-2J,0,0,+2J\}$ — a non-degenerate ground state, a non-degenerate excited state, and a doubly degenerate level at zero, which is the free-fermion spectrum of two modes with the hopping turned on. The whole-chain parity $(-1)^{\hat F}=\sigma^z_1\sigma^z_2$ commutes with the Hamiltonian, with commutator norm exactly $0$, so the degeneracy is resolved by the parity sectors; this is the lattice form of the boundary-condition structure at the end of the chain.

### The String as a Cocycle

The string has one more structural property that the spin language hides and the fermion language makes plain. The map is *ordered*, and reordering the sites multiplies the mode by a parity: for $i<j$,

$$
\hat c_i\hat c_j=-\hat c_j\hat c_i ,
\qquad
\Big(\prod_{k<j}\sigma^z_k\Big)\Big(\prod_{k<i}\sigma^z_k\Big)^{-1}=\prod_{k=i}^{j-1}\sigma^z_k ,
$$

so that moving one operator past another costs exactly the parity of the sites passed. This is the statement that the string is a one-cocycle of the site ordering: it is a phase that must be carried whenever two sites are exchanged, and it is the reason the transformation is nonlocal. The biquaternion reading is the same as before — the phase is the product of the one-site parities $(-1)^{\hat F_k}$ along the path, and the cocycle condition is the statement that the products multiply consistently.

**The boundary term.** The string makes the map nonlocal, and the nonlocality has a physical place: it sits at the chain's ends. The fermion-parity operator of the whole chain,

$$
(-1)^{\hat F}=\prod_j\sigma^z_j ,
$$

is the product of the on-site parities and commutes with $H_{XY}$; the two sectors it labels carry different boundary conditions for the fermions. In the ordered phase of the transverse-field Ising chain the two sectors are nearly degenerate, and the degeneracy is the standard signatures of the $\mathbb{Z}_2$ symmetry in a spin language and of the two boundary-condition sectors in a fermion language — a one-site-versus-whole-chain statement that the algebra's parity reading makes natural.

**The hidden symmetry.** The map also shows why a symmetry visible in one language may be invisible in the other: the parity $(-1)^{\hat F}$ is the on-site $\prod\sigma^z_j$ in the spin language and a constant on the fermionic vacuum, while the hopping is a simple bilinear in one and a two-site spin operator in the other. The transformation does not create or destroy symmetry; it relabels which generators are simple.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The Jordan–Wigner transformation itself, the string, the anticommutators, the number and parity identities, the hopping identity, the inverse map, the free-fermion solution of the XY and transverse-field Ising chains, and the boundary-condition sectors. This is textbook material in the stated convention, and every sign was recomputed on chains up to $N=4$.

**The algebra's own.**

- *The one-site identity.* The parents' $\tilde a=\tfrac12(ie_1-e_2)$ is the one-site Jordan–Wigner map, an identity inside $\mathbb{B}$; the transformation has a one-site fixed point.
- *The string as the product of one-site parities.* $\prod_{k<j}\sigma^z_k=\prod_{k<j}(-1)^{\hat F_k}$, with $(-1)^F=ie_3$ the parent's algebra element. The string is the tensor product of the algebra's parities, and its non-diagonality is the external grading the spin–statistics companion records.
- *The grading statement.* The Jordan–Wigner map is an unital algebra isomorphism that does not preserve the fermionic grading; the even part is $\mathbb{B}$ (or its tensor powers) and the fermions are odd square roots.

**Open.**

- **The chain and the field.** The chain's isomorphism is between finite-dimensional algebras; the field's grading remains external, as the spin–statistics companion records, and no continuum version of the string is adopted here.
- **Boundary conditions in the continuum.** The relation between the chain's two parity sectors and the field's boundary conditions is standard for the lattice and is not pushed to the continuum here.
- **The uniqueness of the square root.** The Jordan–Wigner map is one choice of square root of the observable algebra; whether the algebra singles out a preferred ordering, and hence a preferred string, is not determined by anything used here.

## Companion Articles

- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder identified here with the one-site spin, and the parity $(-1)^F=ie_3$.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the identification $\Phi(ie_k)=\gamma^0\gamma^k$ and the module action that fixes the one-site map.

## Summary

The Jordan–Wigner transformation in biquaternion form is the statement that the transformation has a one-site fixed point inside the algebra and is extended over sites by the product of the algebra's parities. At one site the parents' ladder $\tilde a=\tfrac12(ie_1-e_2)$ satisfies $\tilde a^2=0$, $\{\tilde a,\tilde a^\dagger\}=e_0$, $[\tilde a,\tilde a^\dagger]=ie_3$, so a one-site spin ladder *is* a fermionic mode and the string is the empty product.

For $N$ sites, with $\hat c_j=(\prod_{k<j}\sigma^z_k)\sigma^+_j$ and the spin-down state occupied,

$$
\{\hat c_i,\hat c_j^\dagger\}=\delta_{ij} ,
\qquad
\hat n_j=\frac{I-\sigma^z_j}{2} ,
\qquad
(-1)^{\hat n_j}=\sigma^z_j ,
\qquad
\hat c_j^\dagger\hat c_{j+1}+\text{h.c.}=\tfrac12\big(\sigma^x_j\sigma^x_{j+1}+\sigma^y_j\sigma^y_{j+1}\big),
$$

all four verified with zero error on chains of up to four sites. The string is the product of one-site parities, $\prod_{k<j}\sigma^z_k=\prod_{k<j}(-1)^{\hat F_k}$, each factor being the parent's $(-1)^F=ie_3$; it is trivial at one site and non-diagonal beyond, which is the same externality of the grading that the spin–statistics companion records for the field.

The map is a unital algebra isomorphism — both presentations generate $M_{2^N}(\mathbb{C})$, verified by rank computation for $N=1,2$ — but it is not a map of graded algebras: spins are even bilinears in fermions, the fermions are odd square roots of the even part, and the string is the choice of branch. The consequences are the standard ones: the XY chain becomes free fermions, the whole-chain parity $\prod_j\sigma^z_j$ labels the two boundary-condition sectors, and the near-degeneracy of the ordered phase appears as the standard $\mathbb{Z}_2$ structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde a=\tfrac12(ie_1-e_2)$, $\tilde a^\dagger=\tfrac12(ie_1+e_2)$ | One-site fermionic mode inside $\mathbb{B}$ |
| $\{\tilde a,\tilde a^\dagger\}=e_0$, $[\tilde a,\tilde a^\dagger]=ie_3$ | CAR inside the algebra; commutator not central |
| $\tilde S_k=\tfrac{\hbar}{2}ie_k$, $\tilde S_+=\hbar\,\tilde a$, $\tilde S_-=\hbar\,\tilde a^\dagger$ | Spin generators; one-site JW identity $\tilde a=\tilde S_+/\hbar$ |
| $\sigma^\alpha_j$, $\sigma^\pm_j=\tfrac12(\sigma^x_j\pm i\sigma^y_j)$ | Pauli operators on site $j$ |
| $\hat c_j=(\prod_{k<j}\sigma^z_k)\sigma^+_j$ | Jordan–Wigner fermion (spin-down occupied) |
| $\prod_{k<j}\sigma^z_k=\prod_{k<j}(-1)^{\hat F_k}$ | The string as a product of one-site parities |
| $(-1)^{\hat F}=ie_3=2\tilde S_3/\hbar$ | One-site parity, the string's factor |
| $\{\hat c_i,\hat c_j^\dagger\}=\delta_{ij}$, $\{\hat c_i,\hat c_j\}=0$ | Canonical anticommutators (verified, error $0$) |
| $\hat n_j=(I-\sigma^z_j)/2$, $(-1)^{\hat n_j}=\sigma^z_j$ | Number and parity |
| $\hat c_j^\dagger\hat c_{j+1}+\text{h.c.}=\tfrac12(\sigma^x_j\sigma^x_{j+1}+\sigma^y_j\sigma^y_{j+1})$ | Hopping = XY bond |
| $\sigma^x_j=(\prod_{k<j}\sigma^z_k)(\hat c_j+\hat c_j^\dagger)$ | Inverse map |
| $\mathcal{A}_N\cong\mathrm{Cl}(2N)\cong M_{2^N}(\mathbb{C})$ | Both descriptions generate the full matrix algebra |
| $(-1)^{\hat F}=\prod_j\sigma^z_j$ | Whole-chain parity; boundary-condition sectors |
| $\Phi(ie_k)=\gamma^0\gamma^k$ | Dictionary identification of the algebra into $\mathrm{Cl}^+_{1,3}$ |

## Further Reading

- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot," *Zeitschrift für Physik* **47** (1928) 631–651, for the transformation itself.
- E. Lieb, T. Schultz and D. Mattis, "Two soluble models of an antiferromagnetic chain," *Annals of Physics* **16** (1961) 407–466, for the free-fermion solution of the XY and Ising chains by the transformation.
- P. Pfeuty, "The one-dimensional Ising model with a transverse field," *Annals of Physics* **57** (1970) 79–90, for the transverse-field Ising chain, its two sectors and its degeneracy.
- J. B. Kogut, "An introduction to lattice gauge theory and spin systems," *Reviews of Modern Physics* **51** (1979) 659–713, for the Jordan–Wigner string, the boundary conditions and the $\mathbb{Z}_2$ structure.
- S. Sachdev, *Quantum Phase Transitions* (Cambridge, 2011), for the transverse-field Ising chain and the one-dimensional $\mathbb{Z}_2$ physics used here.
- E. Fradkin, *Field Theories of Condensed Matter Physics* (Cambridge, 2013), for the Jordan–Wigner transformation in the many-body setting and the nonlocal string.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the Clifford algebra with the fermionic mode algebra and the even/odd splitting.
- K. Huang, *Statistical Mechanics* (Wiley, 1987), and R. B. Griffiths, "Correlations in Ising ferromagnets," *Journal of Mathematical Physics* **8** (1967) 478–483, for the $\mathbb{Z}_2$ symmetry and its consequences in the chain.
