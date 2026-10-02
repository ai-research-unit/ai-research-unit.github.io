
# __Polarised Hodge Structures and the Hodge–Riemann Relations__

## Introduction

A Hodge structure on a real vector space of even weight is a decomposition of its complexification into parts $H^{p,q}$ that are exchanged by complex conjugation; equivalently it is a representation of the circle on the complexification, and the decomposition is read from the eigenspaces of the operator that the circle action defines. A **polarisation** is a form on the space that is compatible with the decomposition and positive in a definite sense, the **Hodge–Riemann relations**; with the polarisation the Hodge structure becomes the linear model of the cohomology of a compact Kähler manifold, the Hodge–Riemann bilinear relations being the positivity that the intersection form satisfies on the primitive cohomology. The polarised Hodge structures of a fixed type form the **period domain**, a homogeneous complex manifold on which the cohomology of a family of varieties traces a horizontal holomorphic map, and the theory is the geometry of these moduli.

The article develops the Hodge decomposition and the Hodge filtration, the **Weil operator** $C$ — the operator of the circle action, whose square is the sign $(-1)^{k}$ on weight $k$ and which is the involution that organizes the decomposition — the polarisation and the two Hodge–Riemann bilinear relations, the **Hodge index theorem** for the signature that follows from the positivity, and the period domain with Griffiths transversality. The motivating example is the cohomology of a compact Kähler manifold with its Hodge decomposition, which is *Hermitian Metrics and the Hodge Theory*; the form that polarises it is the intersection form of *Hermitian Pairings on a Topological Space* and *The Signature Operator*.

The prerequisites are *The Hodge Laplacian* for the harmonic forms and the Hodge decomposition; *Hermitian Metrics and the Hodge Theory* for the Dolbeault cohomology and the Kähler identity that produces the $(p,q)$-decomposition; *Hermitian Pairings on a Topological Space* and the Part I articles *Bilinear Forms* and *Indefinite Inner Product Spaces* for the intersection pairing, the symmetry of a form and the signature; *The Signature Operator* for the middle form and its positivity; and *Transformation Groups and the Erlangen Program* and the Lie group articles for the homogeneous space that the period domain is. The analytic existence theory of the Kähler structure and the theory of moduli of varieties belong to other categories and are cited; a Hodge structure here is an algebraic object. No physics is invoked.

## Hodge Structures

**Definition.** A **Hodge structure of weight $k$** on a finitely generated real vector space $V$ is a decomposition of the complexification

$$
V_{\mathbb{C}}=\bigoplus_{p+q=k}H^{p,q},\qquad \overline{H^{p,q}}=H^{q,p},
$$

with the **Hodge numbers** $h^{p,q}=\dim_{\mathbb{C}}H^{p,q}$; the structure is **of type** $(h^{p,q})$. Complex conjugation interchanges the two parts, so $h^{p,q}=h^{q,p}$, and the numbers determine the structure only up to isomorphism of the decomposition. The **Hodge filtration** is the decreasing filtration

$$
F^{p}=\bigoplus_{r\geq p}H^{r,k-r},\qquad
F^{0}=V_{\mathbb{C}}\supseteq F^{1}\supseteq\cdots ,
$$

which recovers the decomposition by $H^{p,q}=F^{p}\cap\overline{F^{q}}$; giving the decomposition is equivalent to giving the filtration, since the filtration alone determines the $H^{p,q}$ through this intersection.

**Example (the cohomology of a Kähler manifold).** Let $X$ be a compact Kähler manifold. The Hodge decomposition

$$
H^{k}(X;\mathbb{C})=\bigoplus_{p+q=k}H^{p,q}(X),\qquad H^{p,q}(X)\cong H^{q}(X,\Omega^{p}),
$$

with $\overline{H^{p,q}}=H^{q,p}$, makes $H^{k}(X;\mathbb{R})$ a Hodge structure of weight $k$; the decomposition is by the $(p,q)$-type of the harmonic representatives and is the Dolbeault cohomology of *Hermitian Metrics and the Hodge Theory*. For $X$ of complex dimension $n$ the numbers satisfy the symmetry $h^{p,q}=h^{q,p}=h^{n-p,n-q}$, the last by Serre duality, and they compute the Betti numbers, $b_{k}=\sum_{p+q=k}h^{p,q}$.

**Definition.** A **morphism of Hodge structures** of the same weight is a linear map that is defined over $\mathbb{Q}$ (or $\mathbb{Z}$) and preserves the decomposition, $f(H^{p,q})\subseteq H^{p,q}$; the Hodge structures of a fixed weight form an abelian category, and the **Tate twist** $V(1)$ multiplies the weight by $-2$ and shifts the bidegree by $(1,1)$.

## The Involution and the Weil Operator

**Definition.** The **Weil operator** of a Hodge structure of weight $k$ is the $\mathbb{C}$-linear operator that acts on $H^{p,q}$ by the scalar

$$
C=i^{\,p-q},
$$

so that $C^2=(-1)^{k}\,\mathrm{id}$ on $V_{\mathbb{C}}$: it is an involution for even weight and a complex structure for odd weight. It commutes with the conjugation in the sense that $C\overline{x}=\overline{Cx}$, and the Hodge structure is recovered from $C$ together with the conjugation.

**Theorem.** The Hodge structures of weight $k$ on $V$ correspond to the real representations of the group $\mathbb{U}(1)$ on $V$ of the form $z\mapsto z^{p}\bar z^{q}$ on $H^{p,q}$, and the Weil operator is the value of the representation at the element $i$; the operator $C$ determines the decomposition as its eigenspaces, and $C^2=(-1)^{k}$.

**Proof.** The representation $z\mapsto z^{p-q}$ on $H^{p,q}$ has derivative data that fix the bidegree; the operator $C$ is the value at $i$, whose eigenspaces are the $H^{p,q}$ because $i^{p-q}$ takes the value $i^{r}$ on the diagonal $p-q=r$; the sum of the eigenspaces is the complexification, and the conjugation condition is the reality of the representation. $\square$

**Remark.** The Weil operator is the involution on the elements of the Hodge structure: the conjugation $\bar\cdot$ is an antilinear involution and $C$ is the linear order-two-up-to-sign operator, and together they generate the structure. In the Kähler case $C$ acts on a $(p,q)$-form as multiplication by $i^{p-q}$, and it is the operator whose commutation with the Laplacian is the Hodge decomposition on the level of harmonic forms of *Hermitian Metrics and the Hodge Theory*.

## Polarisation and the Hodge–Riemann Relations

**Definition.** A **polarisation** of a Hodge structure of weight $k$ on $V$ is a form $Q$ on $V$, defined over $\mathbb{Q}$ (or $\mathbb{Z}$), that is $(-1)^{k}$-symmetric and nondegenerate, and satisfies the two **Hodge–Riemann bilinear relations**

$$
Q(H^{p,q},H^{p',q'})=0\quad\text{unless }p'=k-p,\ q'=k-q,
$$

$$
Q\bigl(Cx,\bar x\bigr)>0\quad\text{for every }x\neq0 ;
$$

a Hodge structure with a polarisation is a **polarised Hodge structure**. The first relation is the horizontality of $Q$ with respect to the decomposition; the second is the positivity, and it says that the Hermitian form

$$
\langle x,y\rangle=Q(Cx,\bar y)
$$

is positive definite on $V_{\mathbb{C}}$.

**Theorem.** The second Hodge–Riemann relation makes $\langle x,y\rangle=Q(Cx,\bar y)$ a positive definite Hermitian form on $V_{\mathbb{C}}$; consequently the form $Q$ has a definite signature on the real part of each piece $H^{p,q}$, and the polarisation determines the Hodge numbers through the signature of its restriction to the real forms of the pieces.

**Proof.** The bilinearity and the symmetry of $Q$ give the Hermitian symmetry of $\langle\cdot,\cdot\rangle$, since $Q(Cy,\bar x)=\overline{Q(Cx,\bar y)}$ by the $(-1)^{k}$-symmetry and the reality of $C$; the positivity is the stated relation, and it is a sum of the contributions of the pieces by the first relation. $\square$

**Theorem (Hodge index theorem).** Let $X$ be a compact Kähler manifold of even complex dimension and let $Q$ be the intersection form on its middle cohomology, the polarisation furnished by the $\varepsilon$-Hermitian pairing $\langle u\cup v,[X]\rangle$ of *Hermitian Pairings on a Topological Space*. Then the signature of $Q$ is

$$
\sigma(X)=\sum_{p,q}(-1)^{p}\,h^{p,q}(X),
$$

the alternating sum over the Hodge numbers; for a compact Kähler surface this is $\sigma=h^{0,0}-h^{1,0}-h^{1,1}+h^{2,0}+h^{2,2}-\cdots$, and the positivity of the polarisation on the primitive cohomology is what fixes the signs.

**Proof sketch.** The Hodge–Riemann relations make $\langle x,y\rangle=Q(Cx,\bar y)$ positive definite; decomposing $Q$ by bidegree with the first relation and counting the signs of $i^{p-q}=C$ on the primitive part of each $H^{p,q}$ gives the index of $Q$ as the alternating sum of the Hodge numbers, the primitive decomposition contributing $h^{p,q}$ with the sign $(-1)^{p}$; the computation is the Hodge index theorem, and it is the precise form of the positivity of the middle form. $\square$

**Example.** For the complex projective plane $h^{0,0}=h^{1,1}=h^{2,2}=1$ and the remaining Hodge numbers vanish, so $\sigma=1-1+1=1$; for a $K3$ surface $h^{2,0}=h^{0,2}=1$, $h^{1,1}=20$ and $h^{2,2}=h^{0,0}=1$, so $\sigma=2-20+2=-16$. Both agree with the signature computed in *The Signature Operator*, and they are the standard checks of the Hodge index theorem.

## The Period Domain

**Definition.** Fix a lattice $V_{\mathbb{Z}}$ with a form $Q$ and a type $(h^{p,q})$. The **period domain** $D$ is the set of polarisations of the Hodge structures of that type on $V_{\mathbb{Z}}$; equivalently, it is the set of Hodge filtrations $F^{\bullet}$ satisfying the Hodge–Riemann relations for the fixed form $Q$.

**Theorem.** The period domain is an open subset of a flag manifold and a homogeneous complex manifold

$$
D=G_{\mathbb{R}}/V ,
$$

where $G_{\mathbb{R}}=\operatorname{Aut}(V_{\mathbb{R}},Q)$ is the real form of the orthogonal or symplectic group that preserves $Q$ and $V$ is the compact subgroup preserving the Hodge filtration and the positivity; the tangent space of $D$ at a point is $\operatorname{Hom}(H^{p,q},H^{p-1,q+1})$ modulo the stabiliser.

**Proof.** The flag manifold of filtrations with $\dim F^{p}$ fixed is a complex homogeneous space of $G_{\mathbb{C}}=\operatorname{Aut}(V_{\mathbb{C}},Q)$; the Hodge–Riemann relations are open conditions — an inequality and an incidence condition — so $D$ is an open subset, and the automorphisms of $Q$ act transitively on it with the compact stabiliser $V$ of a polarised structure. The tangent description is the linearisation of the filtration condition. $\square$

**Definition.** A **variation of Hodge structure** over a base $S$ is a local system of lattices with a Hodge filtration varying holomorphically, such that the **Griffiths transversality** holds:

$$
\nabla F^{p}\subseteq\Omega^{1}_{S}\otimes F^{p-1}
$$

for the Gauss–Manin connection $\nabla$. The **period map** assigns to a family of polarised varieties the varying Hodge structure, and Griffiths transversality says that it is horizontal: the differential of the period map lands in the subspace $\bigoplus_{p}\operatorname{Hom}(H^{p,q},H^{p-1,q+1})$ of the tangent space of $D$ and not in the whole of it.

**Remark.** The period domain is the geometric home of polarised Hodge structures: the polarisation is a chosen form, and the domain classifies the structures it polarises, so the whole construction depends on the chosen $Q$ exactly as the boundary between geometry and the form theory requires. The **Hodge locus**, the locus in the base on which a given class remains of type $(p,p)$, is the subject of the theory of the algebraicity of Hodge classes and of the Hodge conjecture, and it is cited here rather than developed.

## Summary

A **Hodge structure of weight $k$** on a real vector space is a decomposition $V_{\mathbb{C}}=\bigoplus_{p+q=k}H^{p,q}$ with $\overline{H^{p,q}}=H^{q,p}$, equivalently a Hodge filtration $F^{\bullet}$; the motivating example is the $(p,q)$-decomposition of the cohomology of a compact Kähler manifold. The **Weil operator** $C=i^{p-q}$ on $H^{p,q}$ is the involution (for even weight) or complex structure (for odd weight) organised by the circle action, $C^2=(-1)^{k}$, and it is the linear operator of the structure. A **polarisation** is a $(-1)^{k}$-symmetric nondegenerate form $Q$ satisfying the two **Hodge–Riemann bilinear relations**, that $Q$ is horizontal for the decomposition and that the Hermitian form $Q(Cx,\bar y)$ is positive definite; the positivity is the exact form of the Hodge index theorem for the cohomology of a Kähler manifold, whose signature is $\sum_{p,q}(-1)^{p}h^{p,q}$, checked on $\mathbb{CP}^{2}$ ($\sigma=1$) and the $K3$ surface ($\sigma=-16$). The polarised structures of a fixed type form the **period domain** $D=G_{\mathbb{R}}/V$, a homogeneous complex manifold on which the period map of a family of varieties is holomorphic and horizontal by **Griffiths transversality**. The polarisation is a chosen form, and the whole structure — the domain, the positivity and the index formula — is its geometry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_{\mathbb{C}}=\bigoplus_{p+q=k}H^{p,q}$ | Hodge decomposition of weight $k$; $\overline{H^{p,q}}=H^{q,p}$ |
| $h^{p,q}=\dim H^{p,q}$ | Hodge numbers |
| $F^{p}=\bigoplus_{r\geq p}H^{r,k-r}$ | Hodge filtration; $H^{p,q}=F^{p}\cap\overline{F^{q}}$ |
| $C=i^{p-q}$ on $H^{p,q}$ | Weil operator, $C^2=(-1)^k$ |
| $Q$, $(-1)^{k}$-symmetric | Polarisation form |
| $Q(H^{p,q},H^{p',q'})=0$ unless $p'=k-p$ | First Hodge–Riemann relation |
| $Q(Cx,\bar x)>0$ | Second Hodge–Riemann relation |
| $\langle x,y\rangle=Q(Cx,\bar y)$ | Positive definite Hermitian form |
| $\sigma(X)=\sum_{p,q}(-1)^ph^{p,q}$ | Hodge index theorem |
| $D=G_{\mathbb{R}}/V$ | Period domain of polarised Hodge structures |
| $\nabla F^{p}\subseteq\Omega^{1}\otimes F^{p-1}$ | Griffiths transversality |

## Further Reading

- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for Hodge structures, the Hodge–Riemann bilinear relations, the Hodge index theorem and the period map.
- Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I, II* (Cambridge University Press, 2002–2003), for the Hodge decomposition, the polarisation and the period domain.
- W. V. D. Hodge, *The Theory and Applications of Harmonic Integrals* (Cambridge University Press, 1941), for the original Hodge theory and the intersection form.
- Pierre Deligne, "Théorie de Hodge II", *Publications Mathématiques de l'IHÉS* **40** (1971), 5–57, for the mixed Hodge structures and the foundations of the theory.
- Phillip A. Griffiths, "Periods of integrals on algebraic manifolds I, II", *American Journal of Mathematics* **90** (1968), 568–626 and 805–865, for the period map and Griffiths transversality.
- James Carlson, Stefan Müller-Stach and Chris Peters, *Period Mappings and Period Domains* (Cambridge University Press, 2003), for the period domain, its complex structure and the variation of Hodge structure.
