# __Similitudes Between the Poisson Bracket and the Quantum Commutator__

## Introduction

Classical Hamiltonian mechanics and quantum physics each equip their observables with a bracket. In classical mechanics the observables are real functions on phase space and the bracket is the **Poisson bracket** $\{f,g\}$. In quantum physics the observables are Hermitian operators and the bracket is the **commutator** $[f,g]$. The two brackets have the same abstract shape — each is bilinear, antisymmetric, and satisfies the Jacobi identity — and the standard statement of the correspondence between the two theories is the assignment

$$
\boxed{\;\{f,g\}\frac{k_m\,\longleftrightarrow}{m\,c\,i}\,[f,g]\;}.
$$

This article is about that assignment: where it holds, and where it fails. Its thesis has to be stated at the outset, because the notation invites the opposite interpretation. The assignment is **not an isomorphism** of the two bracket algebras. It is a leading-order correspondence that becomes exact only in a limit, and the terms that spoil it are not technical noise: they are the content of the relation between the two theories.

Two structural facts organize everything below.

First, **the two brackets are derivations of different algebras**. The Poisson bracket is a derivation of a *commutative* algebra: for fixed $f$ the map $\{f,\cdot\}$ satisfies the Leibniz rule

$$
\{f,gh\} = \{f,g\}\,h + g\,\{f,h\}.
$$

The commutator is a derivation of a *noncommutative* algebra, with the same formal Leibniz rule $[f,g h] = [f,g]h + g[f,h]$. The two derivations can share their structure constants and still not be the same structure, because a derivation is a derivation *of* an algebra, and the algebras differ in the one property that matters here: whether products commute.

Second, **the map that is supposed to relate them is not a homomorphism for products**. Writing $\operatorname{weyl}$ for a quantization map, one has $\operatorname{weyl}(f)\,\operatorname{weyl}(g) \neq \operatorname{weyl}(fg)$ in general. The two properties that would make the correspondence an isomorphism — products to products, brackets to brackets — are mutually inconsistent. The classical algebra is commutative and the quantum algebra is not, so no product-preserving map can send $\{q,p\}=1$ to $[q,p]=\frac{m\,c\,i}{k_m}$. What survives in place of an isomorphism is a **deformation**: the operator product is the classical product corrected by a series in $\frac{m\,c}{k_m}$ whose first term is the Poisson bracket itself, and the residual mismatch appears at order $\frac{m^{2}\,c^{2}}{k_m^{2}}$.

The article verifies the correspondence on two independent pairs of observables — the canonical pair, and the components of angular momentum — and checks the normalization and the sign explicitly, since the sign of a bracket is the classic error. It then exhibits the failure twice: in the square of a single angular-momentum component, where the bracket correspondence is still exact and only the product fails, and in an explicit pair of cubic observables, where the bracket itself fails. It states the $\hbar\to0$ limit carefully, and closes by locating the resemblance inside the biquaternion framework of the companion articles. That last location is a restricted one: the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is finite-dimensional, and it carries the angular-momentum bracket but not the canonical one.

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

In quantum physics the observables are Hermitian operators $f, g, \dots$ on a Hilbert space, and the bracket is the **commutator**

$$
[f,g] = f g - g f.
$$

It, too, is bilinear and antisymmetric, obeys the Jacobi identity, and is a derivation of the operator algebra under operator multiplication:

$$
[f,g h] = [f,g]h + g[f,h].
$$

The proposed correspondence is that if $f$ and $g$ are the quantum operators associated with the classical observables $f$ and $g$, then the normalized commutator reproduces the Poisson bracket,

$$\frac{k_m}{m\,c\,i}[f,g] \;\longleftrightarrow\; \{f,g\}.
$$

Two features of this display must be read correctly before anything is computed from it.

First, the two sides are **objects of different kinds**: the left side is an operator and the right side is a function on phase space. The arrow is therefore not an equality of elements but a statement about a **quantization map** $f\mapsto\operatorname{weyl}(f)$. Whether such a map can be chosen to make the statement exact is the question of the article, and the answer is that it cannot, except in a limiting sense.

Second, the normalization is not free. The factor $1/(\frac{m\,c\,i}{k_m})$ — with the $i$ *in the denominator*, equivalently $-\frac{k_m\,i}{m\,c}$ — is what makes the canonical pair come out with the standard sign. This is checked in the next section.

## The Canonical Pair: Normalisation and Sign

In the position representation, for a system with coordinates $q_i$, the operators are

$$
q_i\,\tilde{Ξ}_{\mathrm{sp}} = q_i\,\tilde{Ξ}_{\mathrm{sp}}, \qquad p_j\,\tilde{Ξ}_{\mathrm{sp}} = -\frac{m\,c\,i}{k_m}\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial  q_j}.
$$

From these definitions,

$$
[q_i,p_j] =\frac{m\,c\,i\,\delta_{ij}}{k_m},\qquad  [q_i,q_j]=0,\qquad  [p_i,p_j]=0.
$$

Dividing the first by $\frac{m\,c\,i}{k_m}$ gives $\delta_{ij}$, which is exactly $\{q_i,p_j\}$; the other two give $0$, which is exactly $\{q_i,q_j\}$ and $\{p_i,p_j\}$. The canonical pair therefore matches, normalization and all:

| Classical | Quantum | $(\frac{k_m}{m\,c\,i})\times$ Quantum |
|---|---|---|
| $\{q_i,q_j\}=0$ | $[q_i,q_j]=0$ | $0$ |
| $\{p_i,p_j\}=0$ | $[p_i,p_j]=0$ | $0$ |
| $\{q_i,p_j\}=\delta_{ij}$ | $[q_i,p_j]=\frac{m\,c\,i\,\delta_{ij}}{k_m}$ | $\delta_{ij}$ |

**The sign.** Because both brackets are antisymmetric, the relative sign of the two is fixed and can be read off the two off-diagonal entries:

$$
\{q_i,p_j\}=+1 \quad\text{while}\quad  \{p_j,q_i\}=-1, \qquad
[q_i,p_j]=+\frac{m\,c\,i}{k_m}\text{while}\quad  [p_j,q_i]=-\frac{m\,c\,i}{k_m}.
$$

So if one associated $\{f,g\}$ with $(\frac{k_m}{m\,c\,i})[g,f]$ instead — the opposite order — the canonical bracket would come out as $-\delta_{ij}$ and the correspondence would carry the wrong sign throughout. The overall sign of the correspondence is thus a genuine convention, and the convention that agrees with the textbook Poisson bracket is the one with $+1$ on $\{q_i,p_j\}$ and the commutator $[q_i,p_j]$ in the same order. Written as an operator identity for the canonical pair, the correspondence reads

$$
[q_i,p_j] =\frac{m\,c\,i}{k_m}\operatorname{weyl}(\{q_i,p_j\}),
$$

which is the form in which the $\frac{m\,c\,i}{k_m}$ and the order are both manifest.

**Dimensions.** For canonical variables the product $q_ip_j$ has the dimensions of action. The Poisson bracket of two observables therefore has dimension $[f]\,[g]/(\text{action})$, while the commutator $[f,g]$ has dimension $[f]\,[g]$; dividing by $\frac{m\,c}{k_m}$ makes the two sides commensurable. The factor $\frac{m\,c}{k_m}$ is not decoration: it supplies the one missing inverse action.

**What the canonical pair does and does not establish.** The three elementary brackets above are reproduced exactly, but they are too simple to test the correspondence: they involve no products of observables, and the failure of the correspondence is a failure that appears when products are differentiated. The next section supplies an independent test in which products are unavoidable.

## Angular Momentum: A Second, Independent Check

The components of orbital angular momentum are

$$
L_{\mathrm{orb},i} = \epsilon_{ijk}\,q_j\,p_k,
$$

with $\epsilon_{ijk}$ the Levi-Civita symbol and summation over repeated indices understood. Each $L_{\mathrm{orb},i}$ is a product of a coordinate and a momentum, so this test uses the multiplicative structure of the algebra and is independent of the canonical test above.

**Classical side.** From the definition of the Poisson bracket and $\{q_i,p_j\}=\delta_{ij}$ one computes

$$
\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\} = \epsilon_{ijk}\,L_{\mathrm{orb},k},
$$

and, for the brackets with the coordinates and momenta,

$$
\{L_{\mathrm{orb},i},q_j\} = \epsilon_{ijk}\,q_k, \qquad \{L_{\mathrm{orb},i},p_j\} = \epsilon_{ijk}\,p_k.
$$

**Quantum side.** With $L_{\mathrm{orb},i} = \epsilon_{ijk}\,q_j\,p_k$ and the canonical commutators, the same computation gives

$$
[L_{\mathrm{orb},i},L_{\mathrm{orb},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,L_{\mathrm{orb},k}}{k_m},
$$

so that

$$\frac{k_m}{m\,c\,i}[L_{\mathrm{orb},i},L_{\mathrm{orb},j}] = \epsilon_{ijk}\,L_{\mathrm{orb},k},
$$

which is the operator image of $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\epsilon_{ijk}L_{\mathrm{orb},k}$. The correspondence holds on this pair as well.

| Classical | Quantum | $(\frac{k_m}{m\,c\,i})\times$ Quantum |
|---|---|---|
| $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\epsilon_{ijk}L_{\mathrm{orb},k}$ | $[L_{\mathrm{orb},i},L_{\mathrm{orb},j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,L_{\mathrm{orb},k}}{k_m}$ | $\epsilon_{ijk}L_{\mathrm{orb},k}$ |
| $\{L_{\mathrm{orb},i},q_j\}=\epsilon_{ijk}q_k$ | $[L_{\mathrm{orb},i},q_j]=\frac{m\,c\,i\,\epsilon_{ijk}\,q_{k}}{k_m}$ | $\epsilon_{ijk}q_k$ |
| $\{L_{\mathrm{orb},i},p_j\}=\epsilon_{ijk}p_k$ | $[L_{\mathrm{orb},i},p_j]=\frac{m\,c\,i\,\epsilon_{ijk}\,p_{k}}{k_m}$ | $\epsilon_{ijk}p_k$ |

**What the resemblance here is.** Both brackets realize the same three-dimensional Lie algebra: on the classical side the Poisson algebra of the $L_{\mathrm{orb},i}$, and on the quantum side the commutator algebra of the $L_{\mathrm{orb},i}$, are both $\mathfrak{su}(2)$, with the same structure constants $\epsilon_{ijk}$ after the factor $1/(\frac{m\,c\,i}{k_m})$ is extracted. This is a genuine and exact resemblance, and it is the reason the correspondence was ever plausible. It is not, however, a general isomorphism: the pair $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}$ works because the observables are quadratic in the canonical variables, and the next sections show that the correspondence is exact whenever either argument is at most quadratic in the canonical variables.

## Where the Resemblance Holds

It is worth stating exactly what the two successful checks establish, because the resemblance is real and the article would be misleading if it were dismissed.

**Both brackets are Lie brackets.** Each is bilinear, antisymmetric, and satisfies Jacobi. In each theory the observables therefore form a Lie algebra, and the bracket of an observable with the Hamiltonian generates the dynamics: $df/dr'_t=\{f,H\}$ classically, $df/dr'_t=(\frac{k_m}{m\,c\,i})[f,H]$ in the Heisenberg picture. The formal parallel between these two evolution equations is the dynamical core of the correspondence.

**The correspondence is exact for quadratic observables.** For the Weyl quantization used below, the difference between the Moyal bracket and the Poisson bracket begins at order $\frac{m^{2}\,c^{2}}{k_m^{2}}$ and involves third derivatives of the observables. Consequently, **if either argument is at most quadratic in the canonical variables, all corrections vanish and the two brackets agree exactly**:
$$
f \text{ or } g \text{ at most quadratic} \quad\Longrightarrow\quad \frac{k_m}{m\,c\,i}[f,g] = \operatorname{weyl}(\{f,g\}).
$$
This single statement covers both checks of the previous sections: the canonical pair is linear, and the angular-momentum components are quadratic. It also explains why the correspondence looked like an isomorphism: the examples one reaches for first are exactly the examples on which it is one.

**The structure constants are the same.** For any Lie algebra generated by observables that are at most quadratic — the Heisenberg algebra of the canonical pair, the $\mathrm{SU}(2)$ of angular momentum, more generally the symplectic algebra — the Weyl map is a Lie algebra isomorphism onto its image. The resemblance is therefore not a coincidence of signs. It is an exact statement on a subalgebra, and the whole difficulty lies in the words "on a subalgebra".

## Where It Breaks: Products and the Derivation Property

Everything that goes wrong is already contained in one question: does the correspondence respect **products**? The Poisson bracket is built from a commutative product, and its Leibniz rule is a statement about that product. The quantum bracket is built from a noncommutative product. A correspondence that preserved products would have to send commuting classical observables to commuting operators, which is impossible.

**The obstruction.** Suppose a quantization map $\operatorname{weyl}$ satisfied $\operatorname{weyl}(fg)=\operatorname{weyl}(f)\,\operatorname{weyl}(g)$ for all observables. Since classical multiplication is commutative, $\operatorname{weyl}(fg)=\operatorname{weyl}(gf)$, hence $\operatorname{weyl}(f)\,\operatorname{weyl}(g)=\operatorname{weyl}(g)\,\operatorname{weyl}(f)$ for all $f,g$. In particular $[q,p]=0$. But the correspondence requires $[q,p]=\frac{m\,c\,i}{k_m}\operatorname{weyl}(\{q,p\})=\frac{m\,c\,i}{k_m}\neq0$. Therefore no product-preserving map can implement the correspondence: **the homomorphism property and the bracket correspondence are mutually exclusive.** The failure is not a defect of a particular quantization scheme; it is forced by the commutativity of the classical algebra.

**A concrete instance.** The classical observable $qp$ is real, so its quantum image must be Hermitian. The symmetric (Weyl) image is
$$
\operatorname{weyl}(qp) = \tfrac12\left(q p+pq\right) = q p -\frac{m\,c\,i}{2\,k_m},
$$
using $[q,p]=\frac{m\,c\,i}{k_m}$, i.e. $pq=q p-\frac{m\,c\,i}{k_m}$. But the product of the images is $\operatorname{weyl}(q)\,\operatorname{weyl}(p)=q p$. Hence
$$
\operatorname{weyl}(q)\,\operatorname{weyl}(p)-\operatorname{weyl}(qp) =\frac{m\,c\,i}{2\,k_m}\neq0.
$$
The mismatch is exactly the order-$\frac{m\,c}{k_m}$ term. It appears because the commutative product $xp$ carries no ordering, while the operator product does; the quantization must symmetrize to keep the image Hermitian, and symmetrization is not multiplication.

**The general expansion.** For the Weyl map the failure has a uniform form:
$$
\operatorname{weyl}(f)\,\operatorname{weyl}(g) = \operatorname{weyl}(fg) +\frac{m\,c\,i}{2\,k_m}\,\operatorname{weyl}(\{f,g\}) + O(\frac{m^{2}\,c^{2}}{k_m^{2}}).
$$
The leading correction to the product is the Poisson bracket itself. This is the precise sense in which the bracket is a derived object: it *measures* the failure of the quantum product to be commutative. It is not an additional structure imposed on top of the product, and it is not independent of it.

**Why the derivation property does not transfer.** The commutator satisfies $[f,g h]=[f,g]h+g[f,h]$, which is the Leibniz rule for a derivation of the *operator* algebra. To read this as the quantum image of the classical Leibniz rule $\{f,gh\}=\{f,g\}h+g\{f,h\}$ one has to replace the products $g h$ and $\operatorname{weyl}(gh)$ by each other — that is, one has to use the homomorphism property, which is exactly what fails. So Leibniz survives as a formal identity in each theory, and fails as a statement about the correspondence between them. The derivation structure is not what is being matched; only the induced Lie bracket is.

**Concrete products of the canonical pair.** The same failure shows up when the classical Leibniz rule is applied to a degree-two example. Classically,
$$
\{q^2,p^2\}=4qp,
$$
and the operator bracket is
$$\frac{k_m}{m\,c\,i}[q^2,p^2] = 2\left(q p+pq\right).
$$
The right side is the Weyl image of $4qp$, since $\operatorname{weyl}(4qp)=4\cdot\tfrac12(q p+pq)$. It is *not* $4q p$: the naive product exceeds the Weyl image by $\frac{2\,m\,c\,i}{k_m}$. The correspondence is repaired only by the symmetrization, and the symmetrization is precisely the acknowledgement that the map is not a homomorphism.

## Where It Breaks: Deformation and the Order-$\frac{m^{2}\,c^{2}}{k_m^{2}}$ Term

The positive content left after the homomorphism is abandoned is that the quantum product is a **deformation** of the classical one. Define the **star product** on functions of $(q,p)$ by
$$
f\star  g = \exp\!\left(\frac{m\,c\,i}{2\,k_m}\Lambda\right) fg,
\qquad
\Lambda[f,g] = \sum_{i}\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right),
$$
where $\Lambda$ is written as a bidifferential operator: it takes two functions and differentiates the first in one slot and the second in the other, so no mark of a side is needed — the arguments say which factor each derivative acts on. Equivalently, on a product with $\Lambda$ written between the two factors, $\Lambda$ carries the derivative of each slot with it, and the two slots are named by the arguments rather than by an arrow. The star product is associative and noncommutative, and to first order in $\frac{m\,c}{k_m}$ it is
$$
f\star  g = fg +\frac{m\,c\,i}{2\,k_m}\{f,g\} + O(\frac{m^{2}\,c^{2}}{k_m^{2}}).
$$
Its antisymmetrization is the **Moyal bracket**
$$
\{\{f,g\}\} =\frac{k_m}{m\,c\,i}\left(f\star  g - g\star  f\right) = \{f,g\} + O(\frac{m^{2}\,c^{2}}{k_m^{2}}),
$$
which satisfies the Jacobi identity and is the Weyl symbol of $(\frac{k_m}{m\,c\,i})[f,g]$. So the operator bracket algebra is the image of the Moyal algebra, and the Moyal bracket is the Poisson bracket corrected at order $\frac{m^{2}\,c^{2}}{k_m^{2}}$. The failure is therefore not merely of order $\frac{m\,c}{k_m}$ in the product; when the brackets themselves are compared, the leading correction is one order higher, at $\frac{m^{2}\,c^{2}}{k_m^{2}}$.

**An explicit pair of cubic observables.** Take $f=q^3$ and $g=p^3$. On the classical side,
$$
\{q^3,p^3\}=9q^2p^2.
$$
On the Moyal side,
$$
\boxed{\;\{\{q^3,p^3\}\} = 9q^2p^2 - \tfrac{3}{2}\frac{m^{2}\,c^{2}}{k_m^{2}}}.
$$
The difference is the pure number $-\tfrac{3}{2}\frac{m^{2}\,c^{2}}{k_m^{2}}$. In operator language it is a multiple of the identity: it is not a function on phase space that happens to be small, it is a constant with no classical counterpart at all, and it does not vanish at any point of phase space. The bracket of two observables that both vanish at the origin has acquired a term that does not.

The operator computation closes the loop. For the Weyl-quantized operators,
$$\frac{k_m}{m\,c\,i}[q^3,p^3] = 9q^2p^2 -\frac{18\,m\,c\,i\,q\,p}{k_m}-\frac{6\,m^{2}\,c^{2}}{k_m^{2}},
$$
and the Weyl symbol of the right side is $9q^2p^2-\tfrac{3}{2}\frac{m^{2}\,c^{2}}{k_m^{2}}$, which is the Moyal bracket above. So the operator bracket, its symbol, and the star-product bracket agree with each other and disagree with the Poisson bracket by an order-$\frac{m^{2}\,c^{2}}{k_m^{2}}$ constant.

**A second case, checked independently of the first.** For $f=q^4$ and $g=p^4$,
$$
\{q^4,p^4\}=16q^3p^3,
\qquad
\{\{q^4,p^4\}\} = 16q^3p^3 -\frac{24\,m^{2}\,c^{2}\,q\,p}{k_m^{2}}.
$$
Here the correction is not a constant but the phase-space function $-\frac{24\,m^{2}\,c^{2}\,q\,p}{k_m^{2}}$, again of order $\frac{m^{2}\,c^{2}}{k_m^{2}}$. The pattern is the same, and it was checked on a different pair from the one that suggested it: the first correction in the Moyal bracket is $O(\frac{m^{2}\,c^{2}}{k_m^{2}})$, is built from third derivatives of the observables, and is therefore invisible exactly when one of them is at most quadratic.

**The failure reaches down to the quadratic case.** The exactness stated for quadratic observables concerns the bracket and not the symbol, and composing two quadratic observables shows the difference. The symbol of the square of a single component is its star square,
$$
L_{\mathrm{orb},z}\star  L_{\mathrm{orb},z} = \big(L_{\mathrm{orb},z}\big)^2 +\frac{m\,c\,i}{2\,k_m}\{L_{\mathrm{orb},z},L_{\mathrm{orb},z}\} -\frac{m^{2}\,c^{2}}{8\,k_m^{2}}\Lambda^2\big(L_{\mathrm{orb},z},L_{\mathrm{orb},z}\big) = \big(L_{\mathrm{orb},z}\big)^2 -\frac{m^{2}\,c^{2}}{2\,k_m^{2}},
$$
The first-order term vanishes because $\{L_{\mathrm{orb},z},L_{\mathrm{orb},z}\}=0$. The series stops at the second order because each application of $\Lambda$ differentiates each slot once and a quadratic survives only two. The second-order coefficient is $-\frac{m^{2}\,c^{2}}{8\,k_m^{2}}$, and $\Lambda^2(L_{\mathrm{orb},z},L_{\mathrm{orb},z})=4$, so the term is $-\frac{m^{2}\,c^{2}}{2\,k_m^{2}}$. Summing the three components,
$$
\sum_i\big(\operatorname{weyl}(L_{\mathrm{orb},i})\big)^2 = \operatorname{weyl}(L^2) - \tfrac{3}{2}\frac{m^{2}\,c^{2}}{k_m^{2}},
$$
where the subtracted term is the constant $\tfrac32\frac{m^{2}\,c^{2}}{k_m^{2}}$ times the identity operator and $L^2=\sum_i(L_{\mathrm{orb},i})^2$. The sum of the three operator squares is therefore not the Weyl image of the classical $L^2$; it is that image shifted by $-\tfrac32\frac{m^{2}\,c^{2}}{k_m^{2}}$. No bracket sees the shift, because a constant has zero Poisson bracket with everything: $\{L^2-\tfrac32\frac{m^{2}\,c^{2}}{k_m^{2}},\cdot\}=\{L^2,\cdot\}$. The shift is invisible to the two exact checks above and to every other bracket, and it is visible only in the product of two images. That is the article's thesis in its smallest instance: on quadratic observables the bracket correspondence holds, and the product correspondence already fails. Groenewold's theorem excludes an exact bracket correspondence over all polynomials; this offset shows that even where the correspondence holds, the product does not follow the bracket.

**What the deformation is and is not.** The star product is an associative product on the same vector space of functions, deforming the pointwise product. The passage
$$
\text{commutative pointwise product} \;\longrightarrow\; \text{star product}
$$
is a *deformation* in the technical sense: the product changes, the underlying space does not, and the change is controlled by $\frac{m\,c}{k_m}$. What does **not** happen is an isomorphism: the Poisson algebra and the commutator algebra are not isomorphic as algebras, and the failure is exactly the ordering obstruction of the previous section. The deformation is the honest replacement for the isomorphism the notation suggests.

## The $\hbar\to0$ Limit

The phrase "$\hbar\to0$" needs care, because $\frac{m\,c}{k_m}$ is a dimensionful constant and is not small or large in itself, and because the operators depend on $\frac{m\,c}{k_m}$.

**The limit of the normalized bracket.** In the position representation $p_j=-\frac{m\,c\,i}{k_m}\partial/\partial q_j$ depends on $\frac{m\,c}{k_m}$, so the operators $f$ do too. The commutator is of order $\frac{m\,c}{k_m}$, and the normalized quantity $(\frac{k_m}{m\,c\,i})[f,g]$ has a finite limit in the following sense: for polynomial observables and Weyl quantization,
$$
\boxed{\;\lim_{\hbar\to0}\operatorname{weyl}^{-1}\!\left(\frac{1}{i\hbar}[f,g]\right) = \{f,g\}\;},
$$
where $\operatorname{weyl}^{-1}$ is the Weyl symbol, read off the operator, and the approach is controlled by the Moyal bracket: the error is $O(\frac{m^{2}\,c^{2}}{k_m^{2}})$. So the Poisson bracket is the leading term of the deformation, and the correspondence becomes exact as a statement about leading terms.

**Why the limit is formal.** What "$\hbar\to0$" means is an expansion in the dimensionless ratio (typical action)$\frac{k_m}{m\,c}$, not a physical process in which a constant of nature is varied. The perturbative terms are the powers of that ratio. The limit is therefore asymptotic in character: it says that a quantum bracket is a classical bracket plus a series, not that classical mechanics is a regime in which the series' later terms are absent.

**The limit is singular for the algebra.** However small the corrections are, they do not vanish for the fixed nonzero value of $\frac{m\,c}{k_m}$ that nature supplies, and — more importantly — they cannot be removed by a change of correspondence. There is no algebra isomorphism whose $\hbar\to0$ limit is the Poisson algebra, because no quantization is a homomorphism (the previous section). The inverse problem, reconstructing the quantum algebra from the Poisson algebra, therefore has no unique solution; the freedom is the ordering ambiguity. The classical limit is thus a limit of a *deformation*, and the deformation's nontriviality — not its limit — is the physical content.

**Relation to the correspondence principle.** Bohr's correspondence principle states that quantum predictions merge with classical ones in the appropriate limit. The bracket correspondence is its infinitesimal, kinematic part: it matches the local structure of the two theories at a point of phase space. The order-$\frac{m^{2}\,c^{2}}{k_m^{2}}$ terms are why the merge is asymptotic rather than exact, and they are why taking the classical limit of a quantum system requires a limit of states or quantum numbers, not merely the substitution of brackets. Two familiar qualifications make the point.

- **Ehrenfest.** The exact quantum statement is $d\langle  A\rangle/dr'_t = (\frac{k_m}{m\,c\,i})\langle[A,H]\rangle$. Replacing the right side by the classical bracket $\{A,H\}$ evaluated on the mean values is legitimate only to leading order; the corrections involve the higher moments of the state (the wave-packet spread) and vanish only in the regime in which that spread is negligible.
- **Spin.** For angular momentum the bracket correspondence is exact, but the limit is nonetheless degenerate: with $S_k=(\frac{m\,c}{2\,k_m})\sigma_k$ for spin-$\tfrac12$, sending $\hbar\to0$ at fixed spin quantum number sends every spin observable to zero. A classical spin vector emerges only in the limit of large quantum number with $\frac{m\,c\,j}{k_m}$ held fixed. The bracket that matched exactly does not by itself produce a classical limit.

## The Resemblance in the Biquaternion Framework

The companion articles express quantum physics in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. It is worth asking what becomes of the correspondence there, because the framework's realization of it is instructive: it exhibits the resemblance exactly in one of the two checks above and not at all in the other.

**The observables.** In the framework the observables of a two-state system are the Hermitian elements
$$
\tilde R_\Psi = r_t\,e_t + i\,\vec r_\Psi, \qquad r_t\in\mathbb{R}, \quad \vec r_\Psi=(r'_x,r'_y,r'_z)\in\mathbb{R}^3,
$$
of the Hermitian subspace $\mathbb{B}_{\Psi}$, with $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$. For two such elements $\tilde{R}_{\Psi,1}=c r_{t,1}\,e_t+i\vec r_{\Psi,1}$ and $\tilde{R}_{\Psi,2}=c r_{t,2}\,e_t+i\vec r_{\Psi,2}$, their **commutator** is
$$
\boxed{\;[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}] = -2\,(\vec r_{\Psi,1}\times\vec r_{\Psi,2})\;},
$$
a pure real quaternion lying in $\mathbb{B}_{\Phi}\cap\mathbb{H}_\mathbb{B}=\mathrm{span}\{\vec e_x,\vec e_y,\vec e_z\}$. The scalar parts $c r_{t,1}\,e_t$ and $c r_{t,2}\,e_t$ are central and drop out. This bracket is a statement of the algebra alone: **it contains no $\frac{m\,c}{k_m}$.** The quaternion product rule $\vec e_j \vec e_k=\epsilon_{jkl}\vec e_l$ for $j\neq k$ fixes it, and $\mathbb{B}\cong M_2(\mathbb{C})$ is a fixed finite-dimensional algebra in which no deformation parameter appears.

**The angular-momentum resemblance, made exact.** The spin observables are the Hermitian elements
$$
\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}\,i\,\vec e_k \in  \mathbb{B}_{\Psi} \quad(\text{spin-}\tfrac12),
$$
whose matrix images under $\vec e_k\mapsto-i\sigma_k$ are $S_k=(\frac{m\,c}{2\,k_m})\sigma_k$. Direct computation from the commutator of two Hermitian elements gives
$$
[\tilde S_{\Psi,i},\tilde S_{\Psi,j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m},
\qquad\text{so}\qquad\frac{k_m}{m\,c\,i}[\tilde S_{\Psi,i},\tilde S_{\Psi,j}] = \epsilon_{ijk}\,\tilde S_{\Psi,k},
$$
which is term for term the operator image of the classical bracket $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\epsilon_{ijk}L_{\mathrm{orb},k}$. The parallel is exact here: after the factor $1/(\frac{m\,c\,i}{k_m})$ is extracted, the spin bracket and the classical bracket have the same structure constants $\epsilon_{ijk}$. The $\frac{m\,c}{k_m}$-free algebraic bracket $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}]=-2(\vec r_{\Psi,1}\times\vec r_{\Psi,2})$ is their common source — the quaternion cross product is the algebraic expression of the same $\mathrm{SU}(2)$ structure — and $\frac{m\,c}{k_m}$ enters only as the scale that converts the dimensionless algebraic direction $i\vec e_k$ into a physical spin. In this realization the normalization factor $1/(\frac{m\,c\,i}{k_m})$ of the correspondence is not a numerical accident to be checked; it is the unit conversion implied by the identification $\tilde S_{\Psi,k}=(\frac{m\,c}{2\,k_m})i\vec e_k$, and the sign is fixed by the orientation of the cross product.

**Where the framework breaks the correspondence.** The canonical pair cannot be realized this way. The relation
$$
[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}] =\frac{m\,c\,i\,e_{t}}{k_m}$$
has **no solution** with $\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\in\mathbb{B}_{\Psi}$: the commutator of two Hermitian elements of $\mathbb{B}$ is a pure real quaternion and has no scalar part, whereas $\frac{m\,c\,i\,e_{t}}{k_m}$ is purely scalar. Equivalently, the trace of the left side vanishes while $\mathrm{Tr}(\frac{m\,c\,i\,e_{t}}{k_m})=\frac{2\,m\,c\,i}{k_m}\neq0$. The obstruction is not special to the biquaternion notation: it is the familiar statement that the Heisenberg algebra has no finite-dimensional representation, and the finite-dimensional matrix algebra $M_2(\mathbb{C})$ is exactly the setting in which no such representation exists. The framework therefore carries the **compact $\mathrm{SU}(2)$ sector** of the correspondence — the angular-momentum bracket, with no $\frac{m\,c}{k_m}$ in the algebra and no deformation — and not the **Heisenberg sector**, in which the correspondence has a parameter to expand in. Of the two independent checks that opened the article, one lives inside $\mathbb{B}$ and one does not.

**What this does and does not show.** It shows that the resemblance between the Poisson bracket and the commutator is not a story that must be told about infinite-dimensional operator algebras from the start: a finite-dimensional algebra already realizes it exactly on the compact, quadratic sector, with the $\frac{m\,c}{k_m}$ supplied by the physical identification. It does not show that the framework realizes the correspondence in general, and it cannot: the deformation that replaces the isomorphism is a statement about a family of products indexed by $\frac{m\,c}{k_m}$, and a single fixed finite-dimensional algebra is not such a family. The order-$\frac{m^{2}\,c^{2}}{k_m^{2}}$ terms of the previous sections have no home in $\mathbb{B}$; they belong to the canonical sector that $\mathbb{B}$ excludes. Reading the correspondence into the biquaternion framework is therefore legitimate for the angular-momentum algebra and unsupported for anything beyond it.

## Summary

The Poisson bracket and the normalized commutator have the same Lie-algebraic shape, and the standard assignment
$$
\{f,g\}\frac{k_m\,\longleftrightarrow}{m\,c\,i}[f,g]
$$
is correct as a **leading-order correspondence**. It was verified here on two independent pairs: the canonical pair, $\{q_i,p_j\}=\delta_{ij}$ against $[q_i,p_j]=\frac{m\,c\,i\,\delta_{ij}}{k_m}$, with the normalization and the sign checked explicitly; and the components of angular momentum, $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\epsilon_{ijk}L_{\mathrm{orb},k}$ against $[L_{\mathrm{orb},i},L_{\mathrm{orb},j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,L_{\mathrm{orb},k}}{k_m}$. Both match exactly, and the reason is structural: both pairs consist of observables at most quadratic in the canonical variables, and for such observables the correspondence is exact.

It is **not an isomorphism**, and this is the article's thesis. The Poisson bracket is a derivation of a commutative algebra and the commutator is a derivation of a noncommutative one; no product-preserving map can send one to the other, because the classical algebra commutes and the quantum algebra does not. The failure is explicit: $\operatorname{weyl}(q)\,\operatorname{weyl}(p)-\operatorname{weyl}(qp)=\frac{m\,c\,i}{2\,k_m}$, and in general $\operatorname{weyl}(f)\,\operatorname{weyl}(g)=\operatorname{weyl}(fg)+(\frac{m\,c\,i}{2\,k_m})\operatorname{weyl}(\{f,g\})+O(\frac{m^{2}\,c^{2}}{k_m^{2}})$. What replaces the isomorphism is a **deformation**: the star product deforms the commutative product, its antisymmetrization is the Moyal bracket, and
$$
\{\{f,g\}\} = \{f,g\} + O(\frac{m^{2}\,c^{2}}{k_m^{2}}).
$$
The leading failure of the bracket correspondence is therefore at order $\frac{m^{2}\,c^{2}}{k_m^{2}}$ — for $f=q^3$, $g=p^3$, the classical bracket $9q^2p^2$ becomes $9q^2p^2-\tfrac32\frac{m^{2}\,c^{2}}{k_m^{2}}$ — and that residual is not small at any point of phase space; it is a constant. The product fails where the bracket does not: the two checks that came out exact are checks of brackets, and the bracket correspondence is exact for observables at most quadratic, yet the square of a single component already carries the offset
$$
\operatorname{weyl}\big(L_{\mathrm{orb},z}\big)\operatorname{weyl}\big(L_{\mathrm{orb},z}\big) = \operatorname{weyl}\Big(\big(L_{\mathrm{orb},z}\big)^2\Big) -\frac{m^{2}\,c^{2}}{2\,k_m^{2}},
$$
so that the sum over the three components lies $\tfrac32\frac{m^{2}\,c^{2}}{k_m^{2}}$ below the Weyl image of $L^2$; no bracket detects the shift, because a constant has zero bracket with everything. The $\hbar\to0$ limit is formal, dimensionful, and singular as an algebra statement: the Poisson algebra is the leading term of a deformation, not the $\hbar=0$ fibre of an isomorphism, and recovering the quantum algebra from it requires choosing an ordering.

In the biquaternion framework, the observables are the Hermitian elements of $\mathbb{B}_{\Psi}$ and the commutator is the $\frac{m\,c}{k_m}$-free algebraic bracket $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}]=-2(\vec r_{\Psi,1}\times\vec r_{\Psi,2})$. The framework realizes the angular-momentum correspondence exactly, with $\frac{m\,c}{k_m}$ entering through the identification $\tilde S_{\Psi,k}=(\frac{m\,c}{2\,k_m})i\vec e_k$, and it cannot realize the canonical one, because the relation $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}]=\frac{m\,c\,i\,e_{t}}{k_m}$ has no solution in $\mathbb{B}_{\Psi}$. The resemblance is real on the compact sector and absent on the sector that carries the deformation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{f,g\}$ | Poisson bracket of classical observables |
| $[f,g]$ | Commutator of quantum observables |
| $\frac{m\,c}{k_m}$ | Reduced Planck constant (dimensionful; $\hbar\to0$ is formal) |
| $q_i, p_j$ | Canonical coordinates and momenta |
| $\delta_{ij}, \epsilon_{ijk}$ | Kronecker delta; Levi-Civita symbol |
| $L_{\mathrm{orb},i}=\epsilon_{ijk}q_jp_k$ | Orbital angular momentum components |
| $q_i, p_j=-\frac{m\,c\,i}{k_m}\partial/\partial q_j$ | Position and momentum operators |
| $\operatorname{weyl}(f)$ | Quantization map (Weyl ordering) |
| $\operatorname{weyl}^{-1}$ | Its inverse, the Weyl symbol of an operator |
| $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\epsilon_{ijk}L_{\mathrm{orb},k}$ | Classical angular-momentum Poisson algebra |
| $L^2=\sum_i(L_{\mathrm{orb},i})^2$ | Squared orbital angular momentum |
| $\star$ | Star product (deformation of the pointwise product) |
| $\Lambda[f,g]=\sum_i(\partial f/\partial q_i\,\partial g/\partial p_i-\partial f/\partial p_i\,\partial g/\partial q_i)$ | Bidifferential operator of the star product, applied slot by slot |
| $\{\{f,g\}\}=(\frac{k_m}{m\,c\,i})(f\star g-g\star f)$ | Moyal bracket |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$; $i$ | Quaternion basis ($\vec e_k^2=-e_t$); scalar imaginary ($i^2=-1$) |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | Hermitian (observables) and anti-Hermitian (generators) subspaces |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\tilde R_\Psi=r_t\,e_t+i\vec r_\Psi$ | Hermitian observable |
| $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}]=-2(\vec r_{\Psi,1}\times\vec r_{\Psi,2})$ | Biquaternion commutator ($\frac{m\,c}{k_m}$-free) |
| $\tilde S_{\Psi,k}=(\frac{m\,c}{2\,k_m})i\vec e_k$ | Spin-$\tfrac12$ observables |
| $\mathrm{Tr}(\tilde Q\tilde R_\Psi)=2\,\mathrm{Sc}(\tilde Q\tilde R_\Psi)$ | Trace formula |

## Further Reading

- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html), for the commutator $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}]=-2(\vec r_{\Psi,1}\times\vec r_{\Psi,2})$ and the spin relations $[\tilde S_{\Psi,i},\tilde S_{\Psi,j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}$ used in the framework section.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the observables in $\mathbb{B}_{\Psi}$, the trace formula, and the dynamics that supply the quantum side of the correspondence.
- [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html), for the identification of $\mathbb{B}_{\Psi}$ with the qubit observables and the isomorphism $\vec e_k\mapsto-i\sigma_k$ used throughout the framework section.
- [The Harmonic Oscillator in Biquaternionic Form](the-harmonic-oscillator-in-biquaternionic-form.html), for the proof that $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}]=\frac{m\,c\,i\,e_{t}}{k_m}$ has no solution in $\mathbb{B}_{\Psi}$ — the trace obstruction that blocks the canonical sector inside $\mathbb{B}$.
- [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html), for the algebra-level meaning of "derivation" and for the inner derivations $\mathrm{ad}_a=[a,\cdot]$, the biquaternion instance of the commutator-as-derivation used in the article.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the role of $\mathbb{B}_{\Psi}$ as the operator space and the reversible/irreversible dichotomy.
- [Quantum Physics: Foundations and Structure](quantum-physics-foundations-and-structure.html), for the postulational account of observables, commutators, and the classical limit against which the correspondence is stated.
- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the Heisenberg-picture dynamics $df/dr'_t=(\frac{k_m}{m\,c\,i})[f,H]$ and the observable/generator split inside the algebra.
- [Deformation Quantization](../articles_maths/deformation-quantization.html), for the star product as a formal associative deformation and for the Moyal product as the closed-form constant-coefficient case.
- [Semiclassical Analysis](../articles_maths/semiclassical-analysis.html), for the Weyl quantisation $\mathrm{Op}^w_{\frac{m\,c}{k_m}}$, the Moyal product and the Poisson-bracket correspondence in the pseudodifferential calculus.
- H. J. Groenewold, "On the Principles of Elementary Quantum Mechanics", *Physica* **12** (1946), 405–446, for the theorem that no quantization map carries the Poisson bracket to the commutator exactly over all polynomials.
- J. E. Moyal, "Quantum Mechanics as a Statistical Theory", *Mathematical Proceedings of the Cambridge Philosophical Society* **45** (1949), 99–124, for the bracket $\{\{f,g\}\}$ and the phase-space formulation it defines.
