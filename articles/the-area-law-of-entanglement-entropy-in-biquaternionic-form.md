# __The Area Law of Entanglement Entropy in Biquaternionic Form__

## Introduction

**The area law** is the geometric statement that the entanglement entropy of a region of a local quantum system is controlled by the size of the region's boundary rather than by the region's volume. For the ground state of a gapped local Hamiltonian in $d$ spatial dimensions,
$$
S_A=\kappa\,\frac{|\partial A|}{\epsilon^{\,d-1}}+\ldots,
$$
where $|\partial A|$ is the area of the boundary, $\epsilon$ is a short-distance cutoff, and the ellipsis stands for subleading terms. It is the field-theoretic output of the replica trick of the preceding article, and it is the entanglement statement of the Bekenstein–Hawking law: the entropy of a black hole is one quarter of its horizon area in Planck units, the most extreme instance of the same scaling.

This article asks what the area law is in the biquaternion framework. The framework is finite-dimensional and carries no ultraviolet divergence and no geometry, so it cannot reproduce the coefficient or the $\epsilon$-dependence. What it can do is reproduce the **structural** content of the law, and that content is exact.

1. **The law is a locality statement, and the framework realizes it discretely.** In a chain of modes, the entropy of a region of a state built by local operations is bounded by the number of bonds crossing the region's boundary, times the logarithm of the bond dimension. Since the biquaternion one-particle module is $\mathbb{C}^2$, each cut contributes at most $\log2$, and the bound is the discrete area law.

2. **A biquaternion chain attains the bound.** For a chain of modes in a product of nearest-neighbour Bell pairs, the entropy of a region is exactly the number of cut pairs times $\log2$ — proportional to the boundary, independent of the region's volume. The article computes this for four modes and regions of one, two, and three sites, verified by partial traces.

3. **The field-theoretic coefficient is imported, not derived.** The $\kappa\,\epsilon^{-(d-1)}$ divergence, the universal subleading constants, the logarithmic violation in gapless systems, the Ryu–Takayanagi area formula, and the Bekenstein–Hawking coefficient are all standard field-theoretic and gravitational results. The framework supplies the finite boundary-proportional structure on which they rest and nothing of their geometric coefficient.

The article proceeds as follows. The area law is stated in its field-theoretic form, with the gapped and gapless cases distinguished and the coefficient discussed. The locality mechanism is explained as a bond-cutting bound, with the finite-depth circuit and matrix-product-state versions. The discrete area law is then realized and verified in the biquaternion chain, with the dimer state and a table of region entropies. The field statement, its holographic and black-hole cases, are recalled. The article closes with the established/interpretation/open split.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, scalar imaginary $i$, and isomorphism $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, so that $\mathbb{B}\cong M_2(\mathbb{C})$. The material and informational subspaces are $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The trace is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, with $\mathrm{Tr}(e_0)=2$; on the tensor power the trace is the product trace. Reduced states and partial traces are those of *Strong Subadditivity in the Biquaternion Framework*, the entanglement entropy and replica moments those of *Entanglement Entropy and the Replica Trick in Biquaternionic Form*, and the one-particle module that of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*.

## The Area Law

### Statement

Let $A$ be a spatial region of a $d$-dimensional local quantum system, with boundary $\partial A$ and complement $\bar A$. For the ground state of a local Hamiltonian with a spectral gap, the entanglement entropy of $A$ takes the form
$$
S_A=\kappa\,\frac{|\partial A|}{\epsilon^{\,d-1}}+c_{d-1}\,\frac{|\partial A|}{\epsilon^{\,d-2}}+\cdots+\text{(universal terms)},
$$
where $\epsilon$ is the short-distance cutoff and the leading term is proportional to the boundary area. The entropy is therefore **not** proportional to the volume of $A$: the degrees of freedom inside $A$ are not independently entangled, and the entanglement is carried by the boundary. The terms with powers of $\epsilon$ are non-universal; the finite terms are universal and are the ones with field-theoretic meaning.

The contrast with a random state makes the statement sharp. A state drawn uniformly from the Hilbert space of a region of $n_A$ qubits has, with high probability, $S_A\simeq\min(n_A,n_B)\log2$ — a **volume law**. A gapped ground state has $S_A=O(|\partial A|)$ — an **area law**. Locality and the gap are what suppress the volume scaling.

### Gapped and Gapless

The dimension and the gap change the law's form, and the cases are standard.

- **Gapped, $d=1$.** The entropy of an interval saturates to a constant independent of its length, $S_A=O(1)$; the area of a point-boundary in one dimension is a constant. This is the statement proved for gapped chains by Hastings.
- **Gapless, $d=1$.** The entropy grows logarithmically, $S_A=\frac{c}{3}\log\frac{L}{\epsilon}$, with $c$ the central charge. This is the one-dimensional conformal field theory result of Holzhey–Larsen–Wilczek and Calabrese–Cardy, and it is the logarithmic violation of the area law.
- **Gapped, $d\ge2$.** The leading term is $\kappa|\partial A|\epsilon^{-(d-1)}$, and there is a universal constant term whose monotonicity under the renormalization group is a theorem in two dimensions (the $F$-theorem).
- **Gapless, $d\ge2$.** The leading term is still boundary-proportional in the cases that are known, with additional logarithmic factors at special points.

The area law is thus the generic behaviour of local ground states, and its violations are signals of gaplessness or of non-locality.

### The Coefficient and the Divergence

Two features of the leading term are field-theoretic and are not accessible in a finite-dimensional model.

- **The divergence.** The coefficient $\kappa\epsilon^{-(d-1)}$ diverges as the cutoff is removed. It is a short-distance quantity: each boundary bond contributes an $O(1)$ amount of entanglement in units of the cutoff, and the total is the number of such bonds, which scales as the boundary area divided by the cutoff area. The divergence is the same one that the replica partition function produces as the branch locus is approached.
- **The coefficient.** The value of $\kappa$ is non-universal for the leading term, and universal for the finite terms. In holography the leading term is fixed by the Ryu–Takayanagi formula, $S_A=\mathrm{Area}(\gamma_A)/(4G_N)$, with $\gamma_A$ the minimal surface homologous to $A$; for a black hole it becomes the Bekenstein–Hawking entropy $S=A_{\mathrm{hor}}/(4G\hbar)$.

## Why Locality Gives an Area Law

### The Bond-Cutting Bound

The mechanism of the area law is a bound, not an exact formula, and the bound is what the finite framework can realize exactly. Consider a chain of $N$ sites, each carrying a Hilbert space of dimension $q$, and suppose the state is built from a product state by a finite-depth circuit of nearest-neighbour gates. Every gate can increase the entanglement across a cut by at most $\log q$; the number of gates that cross the boundary of a region $A$ is at most proportional to $|\partial A|$; and the entanglement of $A$ is bounded by the total entanglement the crossing gates can produce. Hence
$$
S_A\ \le\ |\partial A|\cdot D\cdot\log q,
$$
where $D$ is the circuit depth. In one dimension an interval has $|\partial A|\le2$, so $S_A\le2D\log q$ independent of the interval's length — the one-dimensional area law. In higher dimensions the bound is proportional to the boundary, which is the discrete form of the area law.

The bound is sharp for states that saturate it, and it is the reason local ground states obey the area law: gapped ground states are well approximated by such finite-depth or bounded-bond-dimension constructions, by the Lieb–Robinson bound and its consequences.

### Matrix-Product States

The same content is expressed by the matrix-product representation. A chain state of **bond dimension** $\chi$ has
$$
S_A\le 2\log\chi
$$
for an interval $A$, and the bound is saturated when the transfer matrices are injective. The bond dimension is the number of states the entanglement across a bond can carry: a bond of dimension $\chi$ carries at most $\log\chi$ nats, and an interval's two boundaries carry at most $2\log\chi$ in total. The biquaternion chain has $\chi=2$, the dimension of the one-particle module, so each boundary contributes at most $\log2$ and an interval at most $2\log2$.

The area law is thus the statement that the entanglement of a local state lives on the boundary, with at most $\log(\text{bond dimension})$ per boundary bond. That statement is exact in finite dimension, and it is the framework's version of the law.

## The Discrete Area Law in the Biquaternion Chain

### The Chain and Its Regions

Take a chain of $N$ modes, with the state living in the tensor power
$$
\mathbb{B}^{\otimes N}\cong M_{2^N}(\mathbb{C}),
$$
and let $A$ be a subset of the sites, with reduced state $\rho_A=\mathrm{Tr}_{\bar A}\,\rho$ obtained by the partial trace of the strong-subadditivity companion article. The one-particle module is $\mathbb{C}^2$, so each site carries a qubit and each bond can carry at most $\log2$ of entanglement. The discrete area law is the bound
$$
S_A\ \le\ |\partial A|\,\log2,
$$
where $|\partial A|$ is the number of bonds between $A$ and its complement, together with the structure statement that states built by local operations saturate or approach it. A state whose entropy is proportional to the number of sites is the discrete volume law, and the contrast between the two is the content of the law.

### The Dimer State

The simplest local state that attains the bound is the product of nearest-neighbour Bell pairs — a **dimer state** — in which each pair is maximally entangled and different pairs are uncorrelated. For four sites, label the pairs $(1,2)$ and $(3,4)$ and take
$$
\rho=\big|\Phi^+\big\rangle\big\langle\Phi^+\big|_{(1,2)}
\ \otimes\ \big|\Phi^+\big\rangle\big\langle\Phi^+\big|_{(3,4)},
\qquad
\big|\Phi^+\big\rangle=\frac{1}{\sqrt2}\big(|00\rangle+|11\rangle\big).
$$
Because the two dimers are uncorrelated, the entropy of a region is the number of dimers the region cuts, times $\log2$: a dimer that lies entirely inside or entirely outside contributes nothing, and a dimer that is cut contributes its full $\log2$.

### Verification

The reduced states were computed by explicit partial trace of the $16\times16$ density matrix, and their entropies from the eigenvalues of the reduced matrices. The results are in the table; $|\partial A|$ is the number of cut bonds.

| Region $A$ | sites | $|\partial A|$ | $S_A$ | $|\partial A|\log2$ |
|---|---|---|---|---|
| $\{1\}$ | $1$ | $1$ | $0.693147$ | $0.693147$ |
| $\{2\}$ | $1$ | $2$ | $0.693147$ | $1.386294$ |
| $\{1,2\}$ | $2$ | $0$ | $0$ | $0$ |
| $\{1,4\}$ | $2$ | $2$ | $1.386294$ | $1.386294$ |
| $\{2,3\}$ | $2$ | $2$ | $1.386294$ | $1.386294$ |
| $\{1,2,3\}$ | $3$ | $1$ | $0.693147$ | $0.693147$ |

The table is the discrete area law in the framework. The entropy of the single site $\{1\}$ is $\log2$, the entropy of the two-site region $\{1,2\}$ is zero because it contains a whole dimer, and the entropy of $\{1,2,3\}$ is again $\log2$ because it cuts only the second dimer. In every row the entropy is fixed by the number of **dimers** the region cuts and not by the number of its sites, each cut dimer contributing exactly $\log2$, the entanglement of one bond of the module. The bound $S_A\le|\partial A|\log2$ is likewise saturated in every row but one. The exception is the single interior site $\{2\}$: it cuts the two boundary bonds $(1,2)$ and $(2,3)$, but only the first of these belongs to a dimer the region cuts, so $S_A=\log2$ lies strictly below $|\partial A|\log2=2\log2$. The bound is an inequality, and the dimer state meets it with equality exactly when the region's boundary bonds are precisely the dimers it cuts.

### The Bound from the Module Dimension

The bound is not an accident of the dimer state; it follows from the rank of the reduced state, and the derivation shows why the boundary appears. Suppose the chain state is constructed so that the correlations across each bond are carried by a single two-state ancilla — the biquaternion one-particle module — as in a tensor-network preparation. Then the reduced state $\rho_A$ is the marginal of a state of $A$ together with one ancilla per boundary bond of $A$, so the rank of $\rho_A$ is at most $2^{|\partial A|}$:
$$
\mathrm{rank}\,\rho_A\ \le\ 2^{\,|\partial A|}.
$$
Since the entropy of a state never exceeds the logarithm of its rank,
$$
S_A\ \le\ \log\mathrm{rank}\,\rho_A\ \le\ |\partial A|\log2,
$$
which is the discrete area law. The boundary appears and the volume does not because only the boundary bonds enter the rank bound. With a module of dimension $\chi$ the same argument gives $S_A\le|\partial A|\log\chi$, and the bound is attained when the boundary ancillas are maximally mixed and uncorrelated and each of them belongs to a bond the region cuts — the situation the dimer state realizes wherever its boundary bonds are the dimers it cuts. The framework's contribution to the area law is this rank argument: the entropy per boundary bond is bounded by the logarithm of the dimension of the module that carries the bond.

A state of the same four sites drawn at random would have $S_A\simeq\min(|A|,4-|A|)$ bits at leading order — a volume law: for $A=\{1,2\}$ that is $2\log2$, where the dimer state gives $0$. The dimer state and the random state are the two extremes, and the gap between them is what the area law asserts about local ground states.

### The Replica Moments of the Dimer State

The discrete area law is visible already at the level of the replica moments of the preceding article. A region that cuts $c$ dimers has reduced state
$$
\rho_A=\bigotimes_{k=1}^{c}\frac{1}{2}I_2
=2^{-c}\,I_{2^c},
$$
a maximally mixed state of $2^c$ levels, because each cut dimer leaves a maximally mixed qubit behind and the dimers are uncorrelated. The replica moments are therefore
$$
Z_n=2^{c}\cdot 2^{-cn}=2^{\,c(1-n)},
\qquad
S_n=\frac{1}{1-n}\log 2^{\,c(1-n)}=c\log2,
$$
so **every** Rényi entropy equals the number of cuts times $\log2$: the entanglement spectrum is completely flat, and the area law holds at all Rényi orders, not merely at $n\to1$. The moments were checked at $c=1$ and $c=2$ for $n=2,3,5$: $Z_n=2^{c(1-n)}$ and $S_n=c\log2$ in every case. The exponential form $Z_n=2^{\,|\partial A|(1-n)}$, valid where the boundary bonds are the cut dimers and $c=|\partial A|$, is the discrete image of the field-theoretic statement that the replica partition function's leading behaviour is governed by the boundary, since it is the boundary that fixes the exponent.

## The Area Law in the Field

In quantum field theory the discrete bound becomes the divergent area formula, and the standard results are recalled here as the field-theoretic completion of the finite statement.

- **Free fields.** The entanglement entropy of a region in the vacuum of a free field is computed by the replica trick; the leading term is proportional to the boundary area divided by the cutoff area, with a coefficient that depends on the number and masses of the fields. The classic computations are those of Bombelli, Koul, Lee, and Sorkin and of Srednicki.
- **Conformal field theory.** In $1+1$ dimensions the area law is violated logarithmically, $S_A=\frac{c}{3}\log(L/\epsilon)$, with the coefficient fixed by the central charge. In higher dimensions the leading boundary term persists, with universal subleading constants.
- **Holography.** The Ryu–Takayanagi formula computes the entanglement entropy of a boundary region as the area of the minimal bulk surface divided by $4G_N$; the area law is thereby identified with a geometric area in one higher dimension.
- **Black holes.** The Bekenstein–Hawking entropy $S=A_{\mathrm{hor}}/(4G\hbar)$ is the area law for the horizon, and its derivation from the entanglement of the quantum fields outside the horizon is the subject of the thermodynamic and entanglement derivations of the Einstein equations.

None of these is derived here. Their common structure is the one the finite framework exhibits: the entropy of a region is controlled by the region's boundary, with a fixed contribution per boundary bond, and it is the short-distance limit of that structure that produces the divergent geometric area.

## The Volume Law and Its Suppression

The area law is a statement about which states are physical, and its content is clearest against the volume law it evades. For a pure state drawn uniformly at random from the Hilbert space of $N$ qubits, the average entanglement entropy of a region of $n_A$ sites is
$$
\overline{S_A}\simeq\min\big(n_A,\,N-n_A\big)\log2,
$$
the **Page curve** (in nats, up to the standard subleading $-\tfrac12$ nat): the entropy grows linearly with the region's size up to half the chain, and is maximal there. It is a volume law: the typical state is maximally entangled across every cut, and the entropy knows nothing about the geometry of the region.

Locality suppresses this. A gapped local ground state has correlations that decay exponentially, its entanglement across a cut is carried by the boundary, and the entropy of a region is governed by $|\partial A|$ rather than by $n_A$. The framework exhibits both extremes in the same algebra: the random state of $\mathbb{B}^{\otimes N}$ has the Page behaviour, while the dimer state — or any state built by a bounded-depth local circuit — has the boundary behaviour $S_A=O(|\partial A|)$. The two differ not in the algebra or in the entropy formula but in how correlated the neighbouring factors are, and that is the whole content of the area law.

The bond dimension quantifies the suppression. An interval of a chain in a matrix-product state of bond dimension $\chi$ satisfies $S_A\le2\log\chi$; a volume-law state requires $\chi$ growing exponentially with $N$, while a gapped ground state admits a $\chi$ independent of $N$. In the framework's chain the module fixes $\chi=2$ at the single-mode level, giving the smallest possible per-bond capacity, and the many-mode module would raise $\chi$ while preserving the boundary proportionality.

## The Area Law and Strong Subadditivity

The entropic inequalities of the strong-subadditivity companion article constrain the area law and are the tools by which it is made stable. Strong subadditivity,
$$
S_{AB}+S_{BC}\ \ge\ S_{B}+S_{ABC},
$$
together with its consequence of monotonicity under coarse-graining, implies that the entanglement of a region cannot increase when the region is extended into its environment or when the system is locally dephased, which is what makes the boundary term the right leading contribution. The universality statements about the subleading terms in the field — for a spherical region in two spatial dimensions, the monotonicity of the constant term under the renormalization group — are consequences of these inequalities applied to the vacuum.

In the finite framework the dimer state and its regions obey strong subadditivity, as every finite-dimensional state does, and the inequalities are visible in the table: the single-site entropy $\log2$ is shared between the two sides of a cut, the two-site region containing a whole dimer has zero entropy, and the entropies are determined by the boundary. The discrete area law and the entropic inequalities are thus statements about the same boundary data, and the framework realizes both exactly.

## What the Framework Does and Does Not Give

**What it gives.** The framework carries a chain of modes, the partial trace that defines a region's reduced state, the entropy of reduced biquaternion states, and the locality bound $S_A\le|\partial A|\log2$ with the module's dimension as the per-bond capacity. The discrete area law is exact and verified; the dimer state shows a state whose entropy sits exactly at the bound for the regions whose boundary bonds are the dimers they cut, and the contrast with a volume-law state is explicit. The statement that locality gives an area law is thus realized at the level of finite-dimensional algebras.

**What it does not give.** The framework has no metric, no dimension $d$, no cutoff, and no ultraviolet divergence, so it cannot produce $\kappa|\partial A|\epsilon^{-(d-1)}$, the universal subleading constants, the logarithmic violation with central charge, the Ryu–Takayanagi surface, or the Bekenstein–Hawking coefficient. Those are field-theoretic and gravitational, and they are imported. The bond dimension of the framework's chain is two; the field's effective bond dimension per cutoff cell is formally infinite, which is why the field's per-bond entropy diverges as the cutoff is removed while the framework's stays $\log2$.

## What Is Established and What Is Interpretation

**Established (theorem, imported).** The field-theoretic area law for gapped ground states; the logarithmic violation in $1+1$-dimensional conformal field theory; the holographic Ryu–Takayanagi formula; the Bekenstein–Hawking entropy; the locality bounds (Lieb–Robinson, Hastings) that make the area law a consequence of the gap and locality. All standard.

**Established (recomputed here).** The bond-cutting bound $S_A\le|\partial A|\log2$ in the biquaternion chain; the dimer state's exact entropy $S_A=(\#\text{cut dimers})\log2$, verified by partial trace for six regions of a four-site chain; and the contrast with the volume law.

**Interpretation.** That the framework's bond dimension two gives the per-boundary-bond capacity of the discrete area law, and that the discrete law is read as the structural content of the field-theoretic area formula. The framework houses the structure; the field supplies the geometry.

**Gaps, left visible.** No metric, no divergence, no coefficient, no subleading universality, no holography. The framework supplies no dynamics and no state selection beyond the toy states used to exhibit the bound. No empirical consequence is derived.

## Open Questions

**1. A biquaternion chain with a genuine gap.** The dimer state is a toy; is there a translation-invariant nearest-neighbour Hamiltonian on $\mathbb{B}^{\otimes N}$ — a modular Hamiltonian of the first-law companion article — whose ground state is gapped and whose regions obey the discrete area law, so that the framework has a Hamiltonian realization of the bound?

**2. The bond dimension and the many-mode module.** The one-particle module is two-dimensional. Is there a natural many-mode module whose bond dimension grows with the mode number, so that the per-bond capacity interpolates between $\log2$ and the field's divergence?

**3. The universal constant term.** In two spatial dimensions the subleading constant in the area law is universal and monotone under the renormalization group. Does the framework's closed-form entropy for biquaternion chains give a finite-size analogue of that term?

**4. The area law and strong subadditivity.** The monotonicity of the area-law coefficient under coarse-graining follows from the entropic inequalities of the companion articles. Does the framework's discrete version give a finite proof of the coefficient's monotonicity, as a one-dimensional chain is coarse-grained?

**5. Empirical contact.** As everywhere in the subcategory, no prediction distinguishing the reading from standard quantum theory is derived.

## Summary

The area law states that the entanglement entropy of a region of a local quantum system is controlled by the region's boundary rather than its volume: for a gapped ground state, $S_A=\kappa|\partial A|\epsilon^{-(d-1)}+\ldots$, with the leading term divergent and non-universal and the subleading terms universal. It is the output of the replica trick in the field, and it is the entanglement form of the Bekenstein–Hawking law.

The area law's mechanism is a locality bound, and the biquaternion framework realizes the bound exactly. In a chain of modes the one-particle module is $\mathbb{C}^2$, so each bond carries at most $\log2$ and a region obeys $S_A\le|\partial A|\log2$; the dimer state attains the bound for the regions whose boundary bonds are the dimers they cut, its entropy $S_A$ being the number of cut dimers times $\log2$, verified by partial trace for six regions of a four-site chain and independent of the region's volume throughout. The contrast with a volume-law random state is the content of the law.

What the framework cannot supply is the geometry: the metric, the dimension, the cutoff, the divergent coefficient, the universal subleading constants, the logarithmic conformal violation, the holographic minimal surface, and the black-hole coefficient are all field-theoretic and gravitational and are imported. The framework's contribution is the exact finite-dimensional boundary-proportional structure — the statement, made precise in the algebra, that a region's entanglement lives on its boundary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $\mathbb{B}^{\otimes N}\cong M_{2^N}(\mathbb{C})$ | Chain of $N$ modes |
| $A,\bar A,\partial A$ | Region, complement, and boundary bonds |
| $\rho_A=\mathrm{Tr}_{\bar A}\,\rho$ | Reduced state of the region |
| $S_A$ | Entanglement entropy of the region |
| $S_A=\kappa|\partial A|\epsilon^{-(d-1)}+\ldots$ | Field-theoretic area law |
| $S_A\le|\partial A|\log2$ | Discrete area-law bound in the framework |
| $\chi$ | Bond dimension; $\chi=2$ for the biquaternion module |
| $|\Phi^+\rangle=\frac{1}{\sqrt2}(|00\rangle+|11\rangle)$ | Bell pair; dimer |
| $S_{BH}=A_{\mathrm{hor}}/(4G\hbar)$ | Bekenstein–Hawking entropy |

## Further Reading

- L. Bombelli, R. K. Koul, J. Lee, and R. D. Sorkin, "Quantum source of entropy for black holes," *Physical Review D* **34** (1986) 373–383, for the first free-field computation of the area law.
- M. Srednicki, "Entropy and area," *Physical Review Letters* **71** (1993) 666–669, for the area law in the free scalar field.
- C. Holzhey, F. Larsen, and F. Wilczek, "Geometric and renormalized entropy in conformal field theory," *Nuclear Physics B* **424** (1994) 443–467, and P. Calabrese and J. Cardy, "Entanglement entropy and quantum field theory," *Journal of Statistical Mechanics* **2004** (2004) P06002, for the logarithmic violation in one dimension.
- M. B. Hastings, "An area law for one-dimensional quantum systems," *Journal of Statistical Mechanics* **2007** (2007) P08024, for the gapped one-dimensional area law.
- J. Eisert, M. Cramer, and M. B. Plenio, "Colloquium: Area laws for the entanglement entropy," *Reviews of Modern Physics* **82** (2010) 277–306, for the general review and the bond-dimension bounds.
- S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from the anti-de Sitter space/conformal field theory correspondence," *Physical Review Letters* **96** (2006) 181602, for the holographic area formula.
- J. D. Bekenstein, "Black holes and entropy," *Physical Review D* **7** (1973) 2333–2346, and S. W. Hawking, "Particle creation by black holes," *Communications in Mathematical Physics* **43** (1975) 199–220, for the Bekenstein–Hawking area law.
- H. Casini and M. Huerta, "A finite entanglement entropy and the c-theorem," *Physics Letters B* **600** (2004) 142–150, for universal subleading terms and their monotonicity.
- E. Witten, "Notes on some entanglement properties of quantum field theory," *Reviews of Modern Physics* **90** (2018) 045003, for the replica geometry and the structure of the divergent terms.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the volume-law behaviour of random states and the bond-dimension picture.
- Companion article *Entanglement Entropy and the Replica Trick in Biquaternionic Form*, for the replica moments that produce the law.
- Companion article *Strong Subadditivity in the Biquaternion Framework*, for reduced states, partial traces, and the tensor powers.
- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-particle module and its dimension.
- Companion article *The Modular Hamiltonian and the First Law of Entanglement in Biquaternionic Form*, for the entanglement Hamiltonian of a region.
- Companion article *The Bisognano–Wichmann Theorem under the Biquaternion Framework*, for the geometric modular structure of a region.
