# __The Cartan Subalgebra, the Roots and the Three Real Forms__

## Introduction

The complexified Lorentz algebra has a two-dimensional Cartan subalgebra, four roots arranged as two orthogonal pairs, and a Weyl group of order four. That much is the root system $A_1\times A_1$, and it is a small, completely explicit object. What it does *not* decide is which real algebra one is talking about, because three different real algebras share the complexification: $\mathfrak{so}(4)$, $\mathfrak{so}(1,3)$ and $\mathfrak{so}(2,2)$.

This article separates the two questions. The root system is a property of the complex algebra: it is the same for all three forms. The real form is a property of a real slice, and it decides which of the six directions are compact, which is to say which of the two triples are compact and whether the physical group has a light cone at all.

The article assumes *The Six Generators and Their Commutators* for the table and the Killing form, and *The Two Commuting Complex Triples* for the split into two summands. It hands the exponential and the global decomposition to *The Exponential Map from Algebra to Group* and the finite carriers to *The Finite-Dimensional Representations and Their Unitarity Defect*.

## The Cartan Subalgebra

### The Definition

A Cartan subalgebra $\mathfrak{h}$ of a semisimple complex Lie algebra is a maximal abelian subalgebra consisting of semisimple elements. For $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ it is two-dimensional, and one convenient choice is

$$
\mathfrak{h}=\operatorname{span}_{\mathbb{C}}\{J_z,K_z\}.
$$

That the span is abelian is read from the table: $[J_z,K_z]=0$. That it is maximal is the dimension count of the next subsection.

### Why Dimension Two

The rank of $\mathfrak{sl}(2,\mathbb{C})$ is one, and the rank of a direct sum is the sum of the ranks, so the rank of the complexified Lorentz algebra is two. The two directions are one from each summand:

$$
\mathfrak{h}=\mathfrak{h}_+\oplus\mathfrak{h}_-,
\qquad \mathfrak{h}_\pm=\operatorname{span}_{\mathbb{C}}\{J_z\pm iK_z\}.
$$

The two lines are the Cartan of the self-dual triple and the Cartan of the anti-self-dual one, and they are complex lines, so the real dimension of $\mathfrak{h}$ is four and its complex dimension two.

### The Three Other Choices

Any rotation of the $z$ axis gives another Cartan, and any boost direction gives another. All Cartans are conjugate under the group, so the choice is a choice of frame and not of algebra. The block fixes the $z$ direction because the eigenvalue computations of the next two articles are done in it.

## The Roots

### The Definition of a Root

A root is a linear functional $\alpha:\mathfrak{h}\to\mathbb{C}$, not zero, for which there is a nonzero $E_\alpha$ with

$$
[H,E_\alpha]=\alpha(H)E_\alpha\quad\text{for all }H\in\mathfrak{h}.
$$

The set of roots is the root system, and the root spaces $E_\alpha$ are the eigenspaces.

### The Four Roots

With $J^\pm=J_x\pm iJ_y$ and $K^\pm=K_x\pm iK_y$, the brackets against the Cartan are

$$
[J_z,J^{\pm}]=\mp iJ^{\pm},\qquad
[K_z,J^{\pm}]=\mp iK^{\pm},\qquad
[J_z,K^{\pm}]=\mp iK^{\pm},\qquad
[K_z,K^{\pm}]=\pm iJ^{\pm}.
$$

The vectors $J^\pm$ and $K^\pm$ are therefore eigenvectors of $J_z$ but not of $K_z$, which mixes the two within each sign. The root vectors of the full Cartan are the combinations

$$
E_1=J^{+}+iK^{+},\quad E_2=J^{+}-iK^{+},\quad
E_3=J^{-}+iK^{-},\quad E_4=J^{-}-iK^{-},
$$

which carry the four roots

$$
\alpha_1=(H_1\mapsto-i,\ H_2\mapsto-1),\quad
\alpha_2=(H_1\mapsto-i,\ H_2\mapsto+1),
$$
$$
\beta_1=(H_1\mapsto+i,\ H_2\mapsto-1),\quad
\beta_2=(H_1\mapsto+i,\ H_2\mapsto+1),
$$

with $H_1=J_z$ and $H_2=K_z$. The $H_1$ entry is imaginary because $J_z$ is anti-Hermitian, and the $H_2$ entry is real because $K_z$ is Hermitian; in the physicist's convention every generator is multiplied by $i$ and the two entries exchange their natures, the $H_1$ values becoming the real $\mp1$. The two conventions differ by the factor $i$ throughout and nothing in this article depends on which is used.

### The Root Spaces

Each root space is one-dimensional, spanned by the root vector named above. The four vectors together with the two Cartan elements span the six-dimensional algebra, so the root decomposition is

$$
\mathfrak{so}(1,3)_{\mathbb{C}}=\mathfrak{h}\oplus\mathbb{C}J^{+}\oplus\mathbb{C}J^{-}\oplus\mathbb{C}K^{+}\oplus\mathbb{C}K^{-}.
$$

That is a direct sum of vector spaces and not of algebras: the root vectors do not commute with each other, and their brackets return Cartan elements.

### Why the Roots Are Not Real Here

The values $\pm i$ are imaginary because the generator $J_z$ is anti-Hermitian. A compact generator has imaginary eigenvalues, and that is the finite-dimensional trace of compactness. In the split picture the Cartan element is not compact and the corresponding root values are real. The point is taken up in §*The Three Real Forms*, because it is exactly the point at which the root system fails to decide the real structure.

## The Root System

### The Two Pairs

The four roots are $\pm\alpha$ and $\pm\beta$, with $\alpha=(H_1\mapsto-i,H_2\mapsto-1)$ and $\beta=(H_1\mapsto-i,H_2\mapsto+1)$. Each pair is a line through the origin in the two-dimensional complex span of the roots.

### The Span Is Two-Dimensional

The two lines are distinct and neither is zero, so they span the two-dimensional space of linear functionals on $\mathfrak{h}$. That is the statement that the rank is two, read dually.

### The Pairing

$$
(\alpha,\beta)=0,
$$

with the inner product induced by the Killing form. The dual metric is $\mathrm{diag}(-\tfrac14,+\tfrac14)$ in the basis dual to $(H_1,H_2)$, because $B(H_1,H_1)=-4$ and $B(H_2,H_2)=+4$, so

$$
(\alpha,\beta)=(-i)(-i)\bigl(-\tfrac14\bigr)+(+1)(-1)\bigl(+\tfrac14\bigr)=\tfrac14-\tfrac14=0 .
$$

The vanishing is the orthogonality of the two summands: $\alpha$ is the root of one and $\beta$ of the other, and $B(J_i,K_j)=0$ by the computation in *The Six Generators and Their Commutators*.

### The Inner Products on the Lines

$$
(\alpha,\alpha)\neq0,\qquad(\beta,\beta)\neq0,
$$

and the two values are equal because the two summands are isomorphic. So the root system is two orthogonal lines of equal length:

$$
A_1\times A_1 .
$$

The two lines are not at $60^{\circ}$ or $45^{\circ}$ or any other angle: they are orthogonal, and that orthogonality is what makes the algebra a direct sum rather than a simple algebra such as $A_2$ or $B_2$.

### What the Shape Decides

The shape of the root system decides the representation theory: two independent lines give two independent highest weights, hence the pair $(m,n)$. It does not decide the real form, because the real form is a real slice and the roots are complex linear functionals.

## The Weyl Group

### The Reflections

For each root $\alpha$ the reflection

$$
s_\alpha(\lambda)=\lambda-2\frac{(\lambda,\alpha)}{(\alpha,\alpha)}\alpha
$$

is an automorphism of the root system. On a root system of two orthogonal equal lines the two reflections act as

$$
s_\alpha(\alpha)=-\alpha,\quad s_\alpha(\beta)=\beta,
\qquad
s_\beta(\beta)=-\beta,\quad s_\beta(\alpha)=\alpha .
$$

### The Group

The two reflections commute and each has order two, so

$$
W\cong\mathbb{Z}_2\times\mathbb{Z}_2,
$$

of order four. It acts on the two-dimensional span of the roots by independent sign changes, which is also the action of the group of diagonal matrices with entries $\pm1$ on the two labels.

### The Action on the Labels

The Weyl group acts on a weight $(m,n)$ by

$$
s_\alpha:(m,n)\longmapsto(-m-1,\,n),\qquad s_\beta:(m,n)\longmapsto(m,\,-n-1),
$$

the affine action with the shift by $\rho$. On the *Casimir* labels, which are $m(m+1)$ and $n(n+1)$, both reflections act trivially, and that is why the two Casimirs are Weyl invariant. On the chiral label, which is $m(m+1)-n(n+1)$, they also act trivially; the chirality is not a Weyl-group effect.

### What the Weyl Group Is Not

The Weyl group is not the Lorentz group, and it is not the rotation group. It is the symmetry of the root system, of order four, and its elements are not exponentials of anything in the algebra. In particular the map $(m,n)\mapsto(n,m)$ is *not* a Weyl reflection: it is the outer automorphism that exchanges the two summands, and it is not inner. This is the algebraic reason the two chiral spinors are not related by a Lorentz transformation.

## The Three Real Forms

### What a Real Form Is

A real form of a complex Lie algebra $\mathfrak{g}$ is a real Lie algebra $\mathfrak{g}_0$ with

$$
\mathfrak{g}_0\otimes_{\mathbb{R}}\mathbb{C}\cong\mathfrak{g}.
$$

Equivalently it is the fixed-point set of a conjugate-linear involution $\sigma$ of $\mathfrak{g}$, the **conjugation**. Two real forms can be non-isomorphic and still have the same complexification, which is the situation here.

### The Compact Form: $\mathfrak{so}(4)$

The real span of the six generators with the brackets of the table **with the sign of the boost–boost block reversed**,

$$
[K_i,K_j]=+J_k,
$$

is $\mathfrak{so}(4)\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, of real dimension six and compact. Its Killing form is negative definite, its Cartan is compact, its roots are imaginary, and every finite-dimensional representation is equivalent to a unitary one.

### The Lorentz Form: $\mathfrak{so}(1,3)$

The real span of the same six with

$$
[K_i,K_j]=-J_k
$$

is $\mathfrak{so}(1,3)\cong\mathfrak{sl}(2,\mathbb{C})$ read as a real algebra. Its Killing form has inertia $(3,3)$, its Cartan has one compact and one non-compact direction, and *as a real algebra it is simple*: it is not a direct sum of two real three-dimensional algebras. This is the form of this block.

### The Split Form: $\mathfrak{so}(2,2)$

$$
\mathfrak{so}(2,2)\cong\mathfrak{sl}(2,\mathbb{R})\oplus\mathfrak{sl}(2,\mathbb{R}),
$$

the real form in which both summands are split. Its Cartan is entirely non-compact, its roots are real, its Killing form has inertia $(4,2)$ — computed in the defining four-vector representation, where the six generators give eigenvalues $-2,-2,+2,+2,+2,+2$ and the two negatives are the two compact rotations — and it is the isometry algebra of a metric with two time and two space directions.

### The Table

| form | real algebra | compact part | Killing inertia $(p,q)$ | Cartan | finite reps unitary? |
|---|---|---|---|---|---|
| $\mathfrak{so}(4)$ | $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ | all six | $(0,6)$ | compact | yes |
| $\mathfrak{so}(1,3)$ | $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ | three, the $J$ | $(3,3)$ | one compact, one not | no |
| $\mathfrak{so}(2,2)$ | $\mathfrak{sl}(2,\mathbb{R})\oplus\mathfrak{sl}(2,\mathbb{R})$ | two, the two rotations | $(4,2)$ | split | no |

This table is the answer to a question that the root system cannot answer. The root system of all three is $A_1\times A_1$; the table's rows differ in the real slice, and the differences are visible in the inertia of the Killing form and in which Cartan directions are compact.

### The Fourth Real Form, for Completeness

The list of real forms of $A_1\times A_1$ contains one more algebra, $\mathfrak{su}(2)\oplus\mathfrak{sl}(2,\mathbb{R})$, whose Killing inertia is $(2,4)$. It is not of the form $\mathfrak{so}(p,q)$ with $p+q=4$, so it is not the isometry algebra of any metric on a four-dimensional real vector space, and the block does not use it. The menu's "three real forms" are the three $\mathfrak{so}(p,q)$'s, and they are the three metrics on $\mathbb{R}^{4}$ up to overall sign.

## The Compact and the Split Picture

### The Compact Picture

In $\mathfrak{so}(4)$ all six generators are rotations of a Euclidean four-space: the three $J$ rotate the $xy$, $yz$ and $zx$ planes and the three $K$ rotate the $xt$, $yt$ and $zt$ planes, and there is no distinguished time direction. The group is $SO(4)$, compact, and every direction in the algebra is conjugate to every other up to the two-block structure. Root values are imaginary, the Casimirs are positive, the exponential map's fibres are the usual ones of a compact group.

### The Split Picture

In $\mathfrak{so}(2,2)$ the two time-like directions of the metric (2,2) mean there are two families of "boosts", one in each time direction, and the compact part is two-dimensional. Root values are real, and the group contains hyperbolic directions in both summands.

### The Mixed Picture and the Physical One

$\mathfrak{so}(1,3)$ is the mixed case: one compact triple and one non-compact. The physics lives here because there is exactly one time direction, and that single fact has three consequences that the block uses constantly.

- There is a light cone: a non-degenerate null cone in the four-vector module, of *The Null Cone: The Massless Boundary*.
- There is a compact maximal subgroup: the rotations, so that angular momentum has discrete spectrum.
- There is a non-compact direction: the boosts, so that a boost has no periodic return and rapidity is unbounded.

None of the three holds in $\mathfrak{so}(4)$, and the third does not hold in the same way in $\mathfrak{so}(2,2)$.

### How the Star Sees the Form

A real form *is* a conjugation, so the star is not an extra structure on top of the real form: it is the real form, written as an involution. Its restriction distinguishes the three cases.

- On $\mathfrak{so}(1,3)$ the star's anti-fixed part in the algebra is the three-dimensional span of the $J$ and its fixed part is the span of the $K$. The star therefore names the Cartan decomposition, and the three non-compact directions are the ones it fixes.
- On $\mathfrak{so}(4)$ the form is the fixed set of its own conjugation and $\dim\mathfrak{k}=6$: the span of the $K$ is not a non-compact piece but three more rotation planes, conjugate to the span of the $J$.
- On $\mathfrak{so}(2,2)$ the conjugation is a third involution and $\dim\mathfrak{k}=2$: two compact directions and four non-compact ones, matching the two time-like directions of the (2,2) metric.

The reader who wants the rule in one line: the star's fixed part in the algebra is the non-compact part, and the compact part is the anti-fixed part. That sentence is true for $\mathfrak{so}(1,3)$ and it is the sense in which this block's star encodes the Lorentzian sign pattern.

## Which Form This Block Uses

### The Answer

$\mathfrak{so}(1,3)$, real dimension six, with the bracket table of *The Six Generators and Their Commutators* and the minus sign in the boost–boost block.

Three statements about it are used so often that they belong here in one place.

- **It is simple as a real algebra.** $\mathfrak{so}(1,3)\cong\mathfrak{sl}(2,\mathbb{C})$ has no proper ideals, so the Lorentz algebra is not a direct sum of two real pieces. Only after complexification does it split.
- **Its complexification splits.** $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$, which is what makes $(m,n)$ a pair of labels.
- **Its compact real form is $\mathfrak{so}(4)$.** So the compact picture is available as a computational device, and it is used exactly where a compact group is easier: the Peter–Weyl theorem, the Weyl unitarian trick, and the convergence of the exponential's fibres.

### What Follows for the Reader

Every formula in the block that mentions $\mathrm{SU}(2)\times\mathrm{SU}(2)$ is a formula about the complexification or about the compact form, and never a formula about the Lorentz group. The block writes $\mathrm{SL}(2,\mathbb{C})$ for the group, $\mathfrak{so}(1,3)$ for the real algebra, $\mathfrak{so}(1,3)_{\mathbb{C}}$ for the complexification, $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ for the compact form, and it keeps them apart.

## Summary

The complexified Lorentz algebra has a two-dimensional Cartan subalgebra, four roots $\pm\alpha$ and $\pm\beta$ spanning a two-dimensional space, and the root system $A_1\times A_1$: two orthogonal lines of equal length. The reflections in the two lines generate a Weyl group $\mathbb{Z}_2\times\mathbb{Z}_2$, which acts trivially on the Casimir labels. The root system is common to three real forms: the compact $\mathfrak{so}(4)\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, the Lorentz form $\mathfrak{so}(1,3)\cong\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$, and the split $\mathfrak{so}(2,2)\cong\mathfrak{sl}(2,\mathbb{R})\oplus\mathfrak{sl}(2,\mathbb{R})$. A real form is a real slice with the same complexification, equivalently the fixed set of a conjugation, and the star is that conjugation. The block uses $\mathfrak{so}(1,3)$, which is simple as a real algebra, splits only after complexification, and has $\mathfrak{so}(4)$ as its compact real form.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathfrak{h}$ | the Cartan subalgebra, spanned by $J_z$ and $K_z$ |
| $\alpha,\beta$ | the two positive roots |
| $J^\pm=J_x\pm iJ_y$, $K^\pm=K_x\pm iK_y$ | the $J_z$-eigenvectors; the roots are carried by $J^\pm\pm iK^\pm$ |
| $A_1\times A_1$ | the root system, two orthogonal equal lines |
| $W\cong\mathbb{Z}_2\times\mathbb{Z}_2$ | the Weyl group |
| $\mathfrak{so}(4)$, $\mathfrak{so}(1,3)$, $\mathfrak{so}(2,2)$ | the three real forms |
| $\sigma$ | the conjugation defining a real form |

## Further Reading

- J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972 — Cartan subalgebras, root systems, Weyl groups and real forms, with $A_1\times A_1$ worked out.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — real forms of a complex semisimple algebra, the classification of $\mathfrak{so}(p,q)$, and the Killing form's inertia.
- A. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002 — real forms, conjugations, and the relation between compact and non-compact pictures.
- R. Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications*, Wiley, 1974 — the $\mathfrak{so}(4)$, $\mathfrak{so}(1,3)$, $\mathfrak{so}(2,2)$ triad in the physicist's notation.
- *The Six Generators and Their Commutators* — the table and the Killing form whose inertia separates the forms.
- *The Exponential Map from Algebra to Group* — the group-level consequences of compactness and its absence.
