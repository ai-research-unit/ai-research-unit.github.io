# __Similitudes Between the Poisson Bracket and the Quantum Commutator__

## Introduction

Classical Hamiltonian mechanics and quantum mechanics each equip their observables with a bracket. In classical mechanics the observables are real functions on phase space and the bracket is the **Poisson bracket** $\{f,g\}$. In quantum mechanics the observables are Hermitian operators and the bracket is the **commutator** $[\hat f,\hat g]$. The two brackets have the same abstract shape — each is bilinear, antisymmetric, and satisfies the Jacobi identity — and the standard statement of the correspondence between the two theories is the assignment

$$
\{f,g\} \;\longleftrightarrow\; \frac{1}{i\hbar}\,[\hat f,\hat g].
$$

This article is about that assignment: where it holds, and where it fails. Its thesis has to be stated at the outset, because the notation invites the opposite reading. The assignment is **not an isomorphism** of the two bracket algebras. It is a leading-order correspondence that becomes exact only in a limit, and the terms that spoil it are not technical noise: they are the content of the relation between the two theories.

Two structural facts organize everything below.

First, **the two brackets are derivations of different algebras**. The Poisson bracket is a derivation of a *commutative* algebra: for fixed $f$ the map $\{f,\cdot\}$ satisfies the Leibniz rule

$$
\{f,gh\} = \{f,g\}\,h + g\,\{f,h\}.
$$

The commutator is a derivation of a *noncommutative* algebra, with the same formal Leibniz rule $[\hat f,\hat g\hat h] = [\hat f,\hat g]\hat h + \hat g[\hat f,\hat h]$. The two derivations can share their structure constants and still not be the same structure, because a derivation is a derivation *of* an algebra, and the algebras differ in the one property that matters here: whether products commute.

Second, **the map that is supposed to relate them is not a homomorphism for products**. Writing $\widehat{\phantom{f}}$ for a quantization map, one has $\widehat f\,\widehat g \neq \widehat{fg}$ in general. The two properties that would make the correspondence an isomorphism — products to products, brackets to brackets — are mutually inconsistent. The classical algebra is commutative and the quantum algebra is not, so no product-preserving map can send $\{q,p\}=1$ to $[\hat q,\hat p]=i\hbar$. What survives in place of an isomorphism is a **deformation**: the operator product is the classical product corrected by a series in $\hbar$ whose first term is the Poisson bracket itself, and the residual mismatch appears at order $\hbar^2$.

The article verifies the correspondence on two independent pairs of observables — the canonical pair, and the components of angular momentum — and checks the normalization and the sign explicitly, since the sign of a bracket is the classic error. It then exhibits the failure on an explicit pair of cubic observables, states the $\hbar\to0$ limit carefully, and closes by locating the resemblance inside the biquaternion framework of the companion articles. That last location is a restricted one: the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is finite-dimensional, and it carries the angular-momentum bracket but not the canonical one.

## The Classical Bracket

Let phase space be $\mathbb{R}^{2n}$ with canonical coordinates $(q_1,\dots,q_n)$ and conjugate momenta $(p_1,\dots,p_n)$. A classical **observable** is a smooth real function $f(q,p)$.

**Definition.** The **Poisson bracket** of two observables is

$$
\{f,g\} = \sum_{i=1}^{n}\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right).
$$

Direct computation from the definition gives the three defining properties.

- **Bilinear and antisymmetric.** $\{f,g\}$ is $\mathbb{R}$-linear in each argument and $\{f,g\}=-\{g,f\}$.
- **Derivation (Leibniz).** $\{f,gh\}=\{f,g\}h+g\{f,h\}$, and likewise in the first argument. For fixed $f$, the operator $X_f=\{f,\cdot\}$ is a **derivation** of the algebra of observables under pointwise multiplication: it is linear and it satisfies the Leibniz rule.
- **Jacobi identity.** $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0$.

The Jacobi identity says that the derivations $X_f$ close under the commutator, so the observables form a Lie algebra — the **Poisson algebra** — and each element acts on the algebra of functions as a derivation. This is the structure that the quantum bracket is conventionally said to resemble.

The elementary brackets are

$$
\{q_i,q_j\}=0,\qquad \{p_i,p_j\}=0,\qquad \{q_i,p_j\}=\delta_{ij}.
$$

The last is the classical statement that positions and momenta are conjugate; the first two say that the coordinates commute as observables. Three brackets used later follow from the definition and, equivalently, from the Leibniz rule:

$$
\{q,p^2\}=2p,\qquad \{q^2,p^2\}=4qp,\qquad \{q^3,p^3\}=9q^2p^2.
$$

The second and third are the cases that will expose the limit of the correspondence, so it is worth noting how little is used to get them: only $\{q,p\}=1$ and Leibniz.

## The Quantum Bracket

In quantum mechanics the observables are Hermitian operators $\hat f, \hat g, \dots$ on a Hilbert space, and the bracket is the **commutator**

$$
[\hat f,\hat g] = \hat f\hat g - \hat g\hat f.
$$

It, too, is bilinear and antisymmetric, obeys the Jacobi identity, and is a derivation of the operator algebra under operator multiplication:

$$
[\hat f,\hat g\hat h] = [\hat f,\hat g]\hat h + \hat g[\hat f,\hat h].
$$

The proposed correspondence is that if $\hat f$ and $\hat g$ are the quantum operators associated with the classical observables $f$ and $g$, then the normalized commutator reproduces the Poisson bracket,

$$
\frac{1}{i\hbar}[\hat f,\hat g] \;\longleftrightarrow\; \{f,g\}.
$$

Two features of this display must be read correctly before anything is computed from it.

First, the two sides are **objects of different kinds**: the left side is an operator and the right side is a function on phase space. The arrow is therefore not an equality of elements but a statement about a **quantization map** $f\mapsto\hat f$. Whether such a map can be chosen to make the statement exact is the question of the article, and the answer is that it cannot, except in a limiting sense.

Second, the normalization is not free. The factor $1/(i\hbar)$ — with the $i$ *in the denominator*, equivalently $-i/\hbar$ — is what makes the canonical pair come out with the standard sign. This is checked in the next section.

## The Canonical Pair: Normalisation and Sign

In the position representation, for a system with coordinates $q_i$, the operators are

$$
\hat q_i\,\psi = q_i\,\psi, \qquad \hat p_j\,\psi = -i\hbar\,\frac{\partial\psi}{\partial q_j}.
$$

From these definitions,

$$
[\hat q_i,\hat p_j] = i\hbar\,\delta_{ij},\qquad [\hat q_i,\hat q_j]=0,\qquad [\hat p_i,\hat p_j]=0.
$$

Dividing the first by $i\hbar$ gives $\delta_{ij}$, which is exactly $\{q_i,p_j\}$; the other two give $0$, which is exactly $\{q_i,q_j\}$ and $\{p_i,p_j\}$. The canonical pair therefore matches, normalization and all:

| Classical | Quantum | $(1/i\hbar)\times$ Quantum |
|---|---|---|
| $\{q_i,q_j\}=0$ | $[\hat q_i,\hat q_j]=0$ | $0$ |
| $\{p_i,p_j\}=0$ | $[\hat p_i,\hat p_j]=0$ | $0$ |
| $\{q_i,p_j\}=\delta_{ij}$ | $[\hat q_i,\hat p_j]=i\hbar\delta_{ij}$ | $\delta_{ij}$ |

**The sign.** Because both brackets are antisymmetric, the relative sign of the two is fixed and can be read off the two off-diagonal entries:

$$
\{q_i,p_j\}=+1 \quad\text{while}\quad \{p_j,q_i\}=-1, \qquad
[\hat q_i,\hat p_j]=+i\hbar \quad\text{while}\quad [\hat p_j,\hat q_i]=-i\hbar.
$$

So if one associated $\{f,g\}$ with $(1/i\hbar)[\hat g,\hat f]$ instead — the opposite order — the canonical bracket would come out as $-\delta_{ij}$ and the correspondence would carry the wrong sign throughout. The overall sign of the correspondence is thus a genuine convention, and the convention that agrees with the textbook Poisson bracket is the one with $+1$ on $\{q_i,p_j\}$ and the commutator $[\hat q_i,\hat p_j]$ in the same order. Written as an operator identity for the canonical pair, the correspondence reads

$$
[\hat q_i,\hat p_j] = i\hbar\,\widehat{\{q_i,p_j\}},
$$

which is the form in which the $i\hbar$ and the order are both manifest.

**Dimensions.** For canonical variables the product $q_ip_j$ has the dimensions of action. The Poisson bracket of two observables therefore has dimension $[f]\,[g]/(\text{action})$, while the commutator $[\hat f,\hat g]$ has dimension $[f]\,[g]$; dividing by $\hbar$ makes the two sides commensurable. The factor $\hbar$ is not decoration: it supplies the one missing inverse action.

**What the canonical pair does and does not establish.** The three elementary brackets above are reproduced exactly, but they are too simple to test the correspondence: they involve no products of observables, and the failure of the correspondence is a failure that appears when products are differentiated. The next section supplies an independent test in which products are unavoidable.

## Angular Momentum: A Second, Independent Check

The components of orbital angular momentum are

$$
L_i = \epsilon_{ijk}\,q_j\,p_k,
$$

with $\epsilon_{ijk}$ the Levi-Civita symbol and summation over repeated indices understood. Each $L_i$ is a product of a coordinate and a momentum, so this test uses the multiplicative structure of the algebra and is independent of the canonical test above.

**Classical side.** From the definition of the Poisson bracket and $\{q_i,p_j\}=\delta_{ij}$ one computes

$$
\{L_i,L_j\} = \epsilon_{ijk}\,L_k,
$$

and, for the brackets with the coordinates and momenta,

$$
\{L_i,q_j\} = \epsilon_{ijk}\,q_k, \qquad \{L_i,p_j\} = \epsilon_{ijk}\,p_k.
$$

**Quantum side.** With $\hat L_i = \epsilon_{ijk}\,\hat q_j\,\hat p_k$ and the canonical commutators, the same computation gives

$$
[\hat L_i,\hat L_j] = i\hbar\,\epsilon_{ijk}\,\hat L_k,
$$

so that

$$
\frac{1}{i\hbar}[\hat L_i,\hat L_j] = \epsilon_{ijk}\,\hat L_k,
$$

which is the operator image of $\{L_i,L_j\}=\epsilon_{ijk}L_k$. The correspondence holds on this pair as well.

| Classical | Quantum | $(1/i\hbar)\times$ Quantum |
|---|---|---|
| $\{L_i,L_j\}=\epsilon_{ijk}L_k$ | $[\hat L_i,\hat L_j]=i\hbar\epsilon_{ijk}\hat L_k$ | $\epsilon_{ijk}\hat L_k$ |
| $\{L_i,q_j\}=\epsilon_{ijk}q_k$ | $[\hat L_i,\hat q_j]=i\hbar\epsilon_{ijk}\hat q_k$ | $\epsilon_{ijk}\hat q_k$ |
| $\{L_i,p_j\}=\epsilon_{ijk}p_k$ | $[\hat L_i,\hat p_j]=i\hbar\epsilon_{ijk}\hat p_k$ | $\epsilon_{ijk}\hat p_k$ |

**What the resemblance here is.** Both brackets realize the same three-dimensional Lie algebra: on the classical side the Poisson algebra of the $L_i$, and on the quantum side the commutator algebra of the $\hat L_i$, are both $\mathfrak{su}(2)$, with the same structure constants $\epsilon_{ijk}$ after the factor $1/(i\hbar)$ is extracted. This is a genuine and exact resemblance, and it is the reason the correspondence was ever plausible. It is not, however, a general isomorphism: the pair $\{L_i,L_j\}$ works because the observables are quadratic in the canonical variables, and the next sections show that the correspondence is exact whenever either argument is at most quadratic in the canonical variables.

## Where the Resemblance Holds

It is worth stating exactly what the two successful checks establish, because the resemblance is real and the article would be misleading if it were dismissed.

**Both brackets are Lie brackets.** Each is bilinear, antisymmetric, and satisfies Jacobi. In each theory the observables therefore form a Lie algebra, and the bracket of an observable with the Hamiltonian generates the dynamics: $\dot f=\{f,H\}$ classically, $\dot{\hat f}=(1/i\hbar)[\hat f,\hat H]$ in the Heisenberg picture. The formal parallel between these two evolution equations is the dynamical core of the correspondence.

**The correspondence is exact for quadratic observables.** For the Weyl quantization used below, the difference between the Moyal bracket and the Poisson bracket begins at order $\hbar^2$ and involves third derivatives of the observables. Consequently, **if either argument is at most quadratic in the canonical variables, all corrections vanish and the two brackets agree exactly**:
$$
f \text{ or } g \text{ at most quadratic} \quad\Longrightarrow\quad \frac{1}{i\hbar}[\hat f,\hat g] = \widehat{\{f,g\}}.
$$
This single statement covers both checks of the previous sections: the canonical pair is linear, and the angular-momentum components are quadratic. It also explains why the correspondence looked like an isomorphism: the examples one reaches for first are exactly the examples on which it is one.

**The structure constants are the same.** For any Lie algebra generated by observables that are at most quadratic — the Heisenberg algebra of the canonical pair, the $\mathfrak{su}(2)$ of angular momentum, more generally the symplectic algebra — the Weyl map is a Lie algebra isomorphism onto its image. The resemblance is therefore not a coincidence of signs. It is an exact statement on a subalgebra, and the whole difficulty lies in the words "on a subalgebra".

## Where It Breaks: Products and the Derivation Property

Everything that goes wrong is already contained in one question: does the correspondence respect **products**? The Poisson bracket is built from a commutative product, and its Leibniz rule is a statement about that product. The quantum bracket is built from a noncommutative product. A correspondence that preserved products would have to send commuting classical observables to commuting operators, which is impossible.

**The obstruction.** Suppose a quantization map $\widehat{\phantom{f}}$ satisfied $\widehat{fg}=\widehat f\,\widehat g$ for all observables. Since classical multiplication is commutative, $\widehat{fg}=\widehat{gf}$, hence $\widehat f\,\widehat g=\widehat g\,\widehat f$ for all $\hat f,\hat g$. In particular $[\hat q,\hat p]=0$. But the correspondence requires $[\hat q,\hat p]=i\hbar\widehat{\{q,p\}}=i\hbar\neq0$. Therefore no product-preserving map can implement the correspondence: **the homomorphism property and the bracket correspondence are mutually exclusive.** The failure is not a defect of a particular quantization scheme; it is forced by the commutativity of the classical algebra.

**A concrete instance.** The classical observable $qp$ is real, so its quantum image must be Hermitian. The symmetric (Weyl) image is
$$
\widehat{qp} = \tfrac12\left(\hat q\hat p+\hat p\hat q\right) = \hat q\hat p - \tfrac{i\hbar}{2},
$$
using $[\hat q,\hat p]=i\hbar$, i.e. $\hat p\hat q=\hat q\hat p-i\hbar$. But the product of the images is $\widehat q\,\widehat p=\hat q\hat p$. Hence
$$
\widehat q\,\widehat p-\widehat{qp} = \tfrac{i\hbar}{2}\neq0.
$$
The mismatch is exactly the order-$\hbar$ term. It appears because the commutative product $qp$ carries no ordering, while the operator product does; the quantization must symmetrize to keep the image Hermitian, and symmetrization is not multiplication.

**The general expansion.** For the Weyl map the failure has a uniform form:
$$
\widehat f\,\widehat g = \widehat{fg} + \frac{i\hbar}{2}\,\widehat{\{f,g\}} + O(\hbar^2).
$$
The leading correction to the product is the Poisson bracket itself. This is the precise sense in which the bracket is a derived object: it *measures* the failure of the quantum product to be commutative. It is not an additional structure imposed on top of the product, and it is not independent of it.

**Why the derivation property does not transfer.** The commutator satisfies $[\hat f,\hat g\hat h]=[\hat f,\hat g]\hat h+\hat g[\hat f,\hat h]$, which is the Leibniz rule for a derivation of the *operator* algebra. To read this as the quantum image of the classical Leibniz rule $\{f,gh\}=\{f,g\}h+g\{f,h\}$ one has to replace the products $\hat g\hat h$ and $\widehat{gh}$ by each other — that is, one has to use the homomorphism property, which is exactly what fails. So Leibniz survives as a formal identity in each theory, and fails as a statement about the correspondence between them. The derivation structure is not what is being matched; only the induced Lie bracket is.

**Concrete products of the canonical pair.** The same failure shows up when the classical Leibniz rule is applied to a degree-two example. Classically,
$$
\{q^2,p^2\}=4qp,
$$
and the operator bracket is
$$
\frac{1}{i\hbar}[\hat q^2,\hat p^2] = 2\left(\hat q\hat p+\hat p\hat q\right).
$$
The right side is the Weyl image of $4qp$, since $\widehat{4qp}=4\cdot\tfrac12(\hat q\hat p+\hat p\hat q)$. It is *not* $4\hat q\hat p$: the naive product differs by $-2i\hbar$. The correspondence is repaired only by the symmetrization, and the symmetrization is precisely the acknowledgement that the map is not a homomorphism.

## Where It Breaks: Deformation and the Order-$\hbar^2$ Term

The positive content left after the homomorphism is abandoned is that the quantum product is a **deformation** of the classical one. Define the **star product** on functions of $(q,p)$ by
$$
f\star g = \exp\!\left(\frac{i\hbar}{2}\Lambda\right) fg,
\qquad
\Lambda = \sum_{i}\left(\overleftarrow{\partial_{q_i}}\,\overrightarrow{\partial_{p_i}} - \overleftarrow{\partial_{p_i}}\,\overrightarrow{\partial_{q_i}}\right),
$$
where the arrows indicate on which factor each derivative acts. The star product is associative and noncommutative, and to first order in $\hbar$ it is
$$
f\star g = fg + \frac{i\hbar}{2}\{f,g\} + O(\hbar^2).
$$
Its antisymmetrization is the **Moyal bracket**
$$
\{\{f,g\}\} = \frac{1}{i\hbar}\left(f\star g - g\star f\right) = \{f,g\} + O(\hbar^2),
$$
which satisfies the Jacobi identity and is the Weyl symbol of $(1/i\hbar)[\hat f,\hat g]$. So the operator bracket algebra is the image of the Moyal algebra, and the Moyal bracket is the Poisson bracket corrected at order $\hbar^2$. The failure is therefore not merely of order $\hbar$ in the product; when the brackets themselves are compared, the leading correction is one order higher, at $\hbar^2$.

**An explicit pair of cubic observables.** Take $f=q^3$ and $g=p^3$. On the classical side,
$$
\{q^3,p^3\}=9q^2p^2.
$$
On the Moyal side,
$$
\{\{q^3,p^3\}\} = 9q^2p^2 - \tfrac{3}{2}\hbar^2.
$$
The difference is the pure number $-\tfrac{3}{2}\hbar^2$. In operator language it is a multiple of the identity: it is not a function on phase space that happens to be small, it is a constant with no classical counterpart at all, and it does not vanish at any point of phase space. The bracket of two observables that both vanish at the origin has acquired a term that does not.

The operator computation closes the loop. For the Weyl-quantized operators,
$$
\frac{1}{i\hbar}[\hat q^3,\hat p^3] = 9\hat q^2\hat p^2 - 18i\hbar\,\hat q\hat p - 6\hbar^2,
$$
and the Weyl symbol of the right side is $9q^2p^2-\tfrac{3}{2}\hbar^2$, which is the Moyal bracket above. So the operator bracket, its symbol, and the star-product bracket agree with each other and disagree with the Poisson bracket by an order-$\hbar^2$ constant.

**A second case, checked independently of the first.** For $f=q^4$ and $g=p^4$,
$$
\{q^4,p^4\}=16q^3p^3,
\qquad
\{\{q^4,p^4\}\} = 16q^3p^3 - 24\hbar^2 qp.
$$
Here the correction is not a constant but the phase-space function $-24\hbar^2 qp$, again of order $\hbar^2$. The pattern is the same, and it was checked on a different pair from the one that suggested it: the first correction in the Moyal bracket is $O(\hbar^2)$, is built from third derivatives of the observables, and is therefore invisible exactly when one of them is at most quadratic.

**What the deformation is and is not.** The star product is an associative product on the same vector space of functions, deforming the pointwise product. The passage
$$
\text{commutative pointwise product} \;\longrightarrow\; \text{star product}
$$
is a *deformation* in the technical sense: the product changes, the underlying space does not, and the change is controlled by $\hbar$. What does **not** happen is an isomorphism: the Poisson algebra and the commutator algebra are not isomorphic as algebras, and the failure is exactly the ordering obstruction of the previous section. The deformation is the honest replacement for the isomorphism the notation suggests.

## The $\hbar\to0$ Limit

The phrase "$\hbar\to0$" needs care, because $\hbar$ is a dimensionful constant and is not small or large in itself, and because the operators depend on $\hbar$.

**The limit of the normalized bracket.** In the position representation $\hat p_j=-i\hbar\partial_{q_j}$ depends on $\hbar$, so the operators $\hat f$ do too. The commutator is of order $\hbar$, and the normalized quantity $(1/i\hbar)[\hat f,\hat g]$ has a finite limit in the following sense: for polynomial observables and Weyl quantization,
$$
\lim_{\hbar\to0}\operatorname{symb}\!\left(\frac{1}{i\hbar}[\hat f,\hat g]\right) = \{f,g\},
$$
where $\operatorname{symb}$ denotes the Weyl symbol, and the approach is controlled by the Moyal bracket: the error is $O(\hbar^2)$. So the Poisson bracket is the leading term of the deformation, and the correspondence becomes exact as a statement about leading terms.

**Why the limit is formal.** What "$\hbar\to0$" means is an expansion in the dimensionless ratio (typical action)$/\hbar$, not a physical process in which a constant of nature is varied. The perturbative terms are the powers of that ratio. The limit is therefore asymptotic in character: it says that a quantum bracket is a classical bracket plus a series, not that classical mechanics is a regime in which the series' later terms are absent.

**The limit is singular for the algebra.** However small the corrections are, they do not vanish for the fixed nonzero value of $\hbar$ that nature supplies, and — more importantly — they cannot be removed by a change of correspondence. There is no algebra isomorphism whose $\hbar\to0$ limit is the Poisson algebra, because no quantization is a homomorphism (the previous section). The inverse problem, reconstructing the quantum algebra from the Poisson algebra, therefore has no unique solution; the freedom is the ordering ambiguity. The classical limit is thus a limit of a *deformation*, and the deformation's nontriviality — not its limit — is the physical content.

**Relation to the correspondence principle.** Bohr's correspondence principle states that quantum predictions merge with classical ones in the appropriate limit. The bracket correspondence is its infinitesimal, kinematic part: it matches the local structure of the two theories at a point of phase space. The order-$\hbar^2$ terms are why the merge is asymptotic rather than exact, and they are why taking the classical limit of a quantum system requires a limit of states or quantum numbers, not merely the substitution of brackets. Two familiar qualifications make the point.

- **Ehrenfest.** The exact quantum statement is $d\langle \hat A\rangle/dt = (1/i\hbar)\langle[\hat A,\hat H]\rangle$. Replacing the right side by the classical bracket $\{A,H\}$ evaluated on the mean values is legitimate only to leading order; the corrections involve the higher moments of the state (the wave-packet spread) and vanish only in the regime in which that spread is negligible.
- **Spin.** For angular momentum the bracket correspondence is exact, but the limit is nonetheless degenerate: with $\hat S_k=(\hbar/2)\sigma_k$ for spin-$\tfrac12$, sending $\hbar\to0$ at fixed spin quantum number sends every spin observable to zero. A classical spin vector emerges only in the limit of large quantum number with $\hbar j$ held fixed. The bracket that matched exactly does not by itself produce a classical limit.

## The Resemblance in the Biquaternion Framework

The companion articles express quantum mechanics in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. It is worth asking what becomes of the correspondence there, because the framework's realization of it is instructive: it exhibits the resemblance exactly in one of the two checks above and not at all in the other.

**The observables.** In the framework the observables of a two-state system are the Hermitian elements
$$
\tilde H = h_0\,e_0 + i\,\mathbf{h}, \qquad h_0\in\mathbb{R}, \quad \mathbf{h}=(h_1,h_2,h_3)\in\mathbb{R}^3,
$$
of the Hermitian subspace $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. Their **commutator** is
$$
[\tilde H,\tilde K] = -2\,(\mathbf{h}\times\mathbf{k}),
$$
a pure real quaternion lying in $\mathbb{M}_-\cap\mathbb{H}_\mathbb{B}=\mathrm{span}\{e_1,e_2,e_3\}$. The scalar parts $h_0e_0$, $k_0e_0$ are central and drop out. This bracket is a statement of the algebra alone: **it contains no $\hbar$.** The quaternion product rule $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$ fixes it, and $\mathbb{B}\cong M_2(\mathbb{C})$ is a fixed finite-dimensional algebra in which no deformation parameter appears.

**The angular-momentum resemblance, made exact.** The spin observables are the Hermitian elements
$$
\tilde S_k = \frac{\hbar}{2}\,i\,e_k \in \mathbb{M}_+ \quad(\text{spin-}\tfrac12),
$$
whose matrix images under $e_k\mapsto-i\sigma_k$ are $\hat S_k=(\hbar/2)\sigma_k$. Direct computation from $[\tilde H,\tilde K]=-2(\mathbf{h}\times\mathbf{k})$ gives
$$
[\tilde S_i,\tilde S_j] = i\hbar\,\epsilon_{ijk}\,\tilde S_k,
\qquad\text{so}\qquad
\frac{1}{i\hbar}[\tilde S_i,\tilde S_j] = \epsilon_{ijk}\,\tilde S_k,
$$
which is term for term the operator image of the classical bracket $\{L_i,L_j\}=\epsilon_{ijk}L_k$. The parallel is exact here: after the factor $1/(i\hbar)$ is extracted, the spin bracket and the classical bracket have the same structure constants $\epsilon_{ijk}$. The $\hbar$-free algebraic bracket $[\tilde H,\tilde K]=-2(\mathbf{h}\times\mathbf{k})$ is their common source — the quaternion cross product is the algebraic expression of the same $\mathfrak{su}(2)$ structure — and $\hbar$ enters only as the scale that converts the dimensionless algebraic direction $ie_k$ into a physical spin. In this realization the normalization factor $1/(i\hbar)$ of the correspondence is not a numerical accident to be checked; it is the unit conversion implied by the identification $\tilde S_k=(\hbar/2)ie_k$, and the sign is fixed by the orientation of the cross product.

**Where the framework breaks the correspondence.** The canonical pair cannot be realized this way. The relation
$$
[\tilde X,\tilde P] = i\hbar\,e_0
$$
has **no solution** with $\tilde X,\tilde P\in\mathbb{M}_+$: the commutator of two Hermitian elements of $\mathbb{B}$ is a pure real quaternion and has no scalar part, whereas $i\hbar e_0$ is purely scalar. Equivalently, the trace of the left side vanishes while $\mathrm{Tr}(i\hbar e_0)=2i\hbar\neq0$. The obstruction is not special to the biquaternion notation: it is the familiar statement that the Heisenberg algebra has no finite-dimensional representation, and the finite-dimensional matrix algebra $M_2(\mathbb{C})$ is exactly the setting in which no such representation exists. The framework therefore carries the **compact $\mathfrak{su}(2)$ sector** of the correspondence — the angular-momentum bracket, with no $\hbar$ in the algebra and no deformation — and not the **Heisenberg sector**, in which the correspondence has a parameter to expand in. Of the two independent checks that opened the article, one lives inside $\mathbb{B}$ and one does not.

**What this does and does not show.** It shows that the resemblance between the Poisson bracket and the commutator is not a story that must be told about infinite-dimensional operator algebras from the start: a finite-dimensional algebra already realizes it exactly on the compact, quadratic sector, with the $\hbar$ supplied by the physical identification. It does not show that the framework realizes the correspondence in general, and it cannot: the deformation that replaces the isomorphism is a statement about a family of products indexed by $\hbar$, and a single fixed finite-dimensional algebra is not such a family. The order-$\hbar^2$ terms of the previous sections have no home in $\mathbb{B}$; they belong to the canonical sector that $\mathbb{B}$ excludes. Reading the correspondence into the biquaternion framework is therefore legitimate for the angular-momentum algebra and unsupported for anything beyond it.

## Summary

The Poisson bracket and the normalized commutator have the same Lie-algebraic shape, and the standard assignment
$$
\{f,g\} \;\longleftrightarrow\; \frac{1}{i\hbar}[\hat f,\hat g]
$$
is correct as a **leading-order correspondence**. It was verified here on two independent pairs: the canonical pair, $\{q_i,p_j\}=\delta_{ij}$ against $[\hat q_i,\hat p_j]=i\hbar\delta_{ij}$, with the normalization and the sign checked explicitly; and the components of angular momentum, $\{L_i,L_j\}=\epsilon_{ijk}L_k$ against $[\hat L_i,\hat L_j]=i\hbar\epsilon_{ijk}\hat L_k$. Both match exactly, and the reason is structural: both pairs consist of observables at most quadratic in the canonical variables, and for such observables the correspondence is exact.

It is **not an isomorphism**, and this is the article's thesis. The Poisson bracket is a derivation of a commutative algebra and the commutator is a derivation of a noncommutative one; no product-preserving map can send one to the other, because the classical algebra commutes and the quantum algebra does not. The failure is explicit: $\widehat q\,\widehat p-\widehat{qp}=i\hbar/2$, and in general $\widehat f\,\widehat g=\widehat{fg}+(i\hbar/2)\widehat{\{f,g\}}+O(\hbar^2)$. What replaces the isomorphism is a **deformation**: the star product deforms the commutative product, its antisymmetrization is the Moyal bracket, and
$$
\{\{f,g\}\} = \{f,g\} + O(\hbar^2).
$$
The leading failure of the bracket correspondence is therefore at order $\hbar^2$ — for $f=q^3$, $g=p^3$, the classical bracket $9q^2p^2$ becomes $9q^2p^2-\tfrac32\hbar^2$ — and that residual is not small at any point of phase space; it is a constant. The $\hbar\to0$ limit is formal, dimensionful, and singular as an algebra statement: the Poisson algebra is the leading term of a deformation, not the $\hbar=0$ fibre of an isomorphism, and recovering the quantum algebra from it requires choosing an ordering.

In the biquaternion framework, the observables are the Hermitian elements of $\mathbb{M}_+$ and the commutator is the $\hbar$-free algebraic bracket $[\tilde H,\tilde K]=-2(\mathbf{h}\times\mathbf{k})$. The framework realizes the angular-momentum correspondence exactly, with $\hbar$ entering through the identification $\tilde S_k=(\hbar/2)ie_k$, and it cannot realize the canonical one, because the relation $[\tilde X,\tilde P]=i\hbar e_0$ has no solution in $\mathbb{M}_+$. The resemblance is real on the compact sector and absent on the sector that carries the deformation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{f,g\}$ | Poisson bracket of classical observables |
| $[\hat f,\hat g]$ | Commutator of quantum observables |
| $\hbar$ | Reduced Planck constant (dimensionful; $\hbar\to0$ is formal) |
| $q_i, p_j$ | Canonical coordinates and momenta |
| $\delta_{ij}, \epsilon_{ijk}$ | Kronecker delta; Levi-Civita symbol |
| $L_i=\epsilon_{ijk}q_jp_k$ | Orbital angular momentum components |
| $\hat q_i, \hat p_j=-i\hbar\partial_{q_j}$ | Position and momentum operators |
| $\widehat{\phantom{f}}$ | Quantization map (Weyl ordering) |
| $\{L_i,L_j\}=\epsilon_{ijk}L_k$ | Classical angular-momentum Poisson algebra |
| $\star$ | Star product (deformation of the pointwise product) |
| $\{\{f,g\}\}=(1/i\hbar)(f\star g-g\star f)$ | Moyal bracket |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0,e_1,e_2,e_3$; $i$ | Quaternion basis ($e_k^2=-e_0$); scalar imaginary ($i^2=-1$) |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian (observables) and anti-Hermitian (generators) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde H=h_0e_0+i\mathbf{h}$ | Hermitian observable |
| $[\tilde H,\tilde K]=-2(\mathbf{h}\times\mathbf{k})$ | Biquaternion commutator ($\hbar$-free) |
| $\tilde S_k=(\hbar/2)ie_k$ | Spin-$\tfrac12$ observables |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula |

## Further Reading

- *Angular Momentum and Spin in Biquaternionic Form* (`articles_physics/angular-momentum-and-spin-in-biquaternionic-form.md`), for the commutator $[\tilde H,\tilde K]=-2(\mathbf{h}\times\mathbf{k})$ and the spin relations $[\tilde S_i,\tilde S_j]=i\hbar\epsilon_{ijk}\tilde S_k$ used in the framework section.
- *Quantum Mechanics in Biquaternionic Form* (`articles_physics/quantum-mechanics-in-biquaternionic-form.md`), for the observables in $\mathbb{M}_+$, the trace formula, and the dynamics that supply the quantum side of the correspondence.
- *Spin-1/2 Quantum Mechanics in Biquaternionic Form* (`articles_physics/spin-1-2-quantum-mechanics-in-biquaternionic-form.md`), for the identification of $\mathbb{M}_+$ with the qubit observables and the isomorphism $e_k\mapsto-i\sigma_k$ used throughout the framework section.
- *The Harmonic Oscillator in Biquaternionic Form* (`articles_physics/the-harmonic-oscillator-in-biquaternionic-form.md`), for the proof that $[\tilde X,\tilde P]=i\hbar e_0$ has no solution in $\mathbb{M}_+$ — the trace obstruction that blocks the canonical sector inside $\mathbb{B}$.
- *Biquaternion Automorphisms and Derivations* (`articles_maths/biquaternion-automorphisms-and-derivations.md`), for the algebra-level meaning of "derivation" and for the inner derivations $\mathrm{ad}_a=[a,\cdot]$, the biquaternion instance of the commutator-as-derivation used in the article.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the role of $\mathbb{M}_+$ as the operator space and the reversible/irreversible dichotomy.
- *Quantum Mechanics: Foundations and Structure* (`articles_physics/quantum-mechanics-foundations-and-structure.md`), for the postulational account of observables, commutators, and the classical limit against which the correspondence is stated.
- *The Schrödinger Equation in Biquaternionic Form* (`articles_physics/the-schrodinger-equation-in-biquaternionic-form.md`), for the Heisenberg-picture dynamics $\dot{\hat f}=(1/i\hbar)[\hat f,\hat H]$ and the observable/generator split inside the algebra.
