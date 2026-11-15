# __The Square Map of the Split-Complex Space__

## Introduction

The square map $\sigma(Q)=Q^2$ is the simplest non-linear map of the split-complex space, and its image, its critical set and its fibres carry the geometry of the ring. This article computes the three: the image is the forward cone $q\ge\lvert q'\rvert$, the critical set is the pair of null lines, and the fibres have four, two, one and no points according to where the value lies.

The square map is not onto, and this is the first difference from the complex field, where the square is onto. The second difference is its critical set: over $\mathbb{C}$ the only critical point is the origin, and here a whole pair of lines is critical. Both differences have one source, the sign $j^2=+1$, which makes the differential $2Q$ singular exactly when $Q$ is a zero divisor.

The product is *The Two Products of the Split-Complex Space*; the roots are *Square Roots of a General Element in the Split-Complex Algebra*, whose four branches this article identifies with the four local inverses; the cone is *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*.

## The Map and Its Coordinates

### The Definition

**Definition.** The **square map** is $\sigma:\mathbb{C}_{\mathrm{spl}}\to\mathbb{C}_{\mathrm{spl}}$, $\sigma(Q)=Q^2$.

On the coordinates $Q=q+jq'$ the map is

$$
\sigma(q,q')=\bigl(q^2+q'^2,\ 2qq'\bigr) ,
$$

a polynomial map of $\mathbb{R}^2$ into itself, of degree two in each coordinate.

### The Idempotent Coordinates

In the idempotent coordinates the map is a squaring in each coordinate separately:

$$
\sigma(Q)_+=Q_+^2, \qquad \sigma(Q)_-=Q_-^2 ,
$$

since $Q^2=(Q_+\Pi_++Q_-\Pi_-)^2=Q_+^2\Pi_++Q_-^2\Pi_-$. The whole geometry of the map is therefore the geometry of the map $t\mapsto t^2$ on the real line, read twice and transported back through the coordinates $Q_\pm=q\pm q'$.

## The Image

### The Forward Cone

**Theorem.** The image of the square map is the forward cone

$$
\mathcal{C}_+=\{q+jq' : q\ge\lvert q'\rvert\}=\{Q : Q_+\ge0\ \text{and}\ Q_-\ge0\} .
$$

**Proof.** A square has non-negative coordinates, $Q_\pm^2\ge0$, so the image lies in the set where both coordinates are non-negative, and that set is the forward cone, since $Q_+\ge0$ and $Q_-\ge0$ read $q\ge\lvert q'\rvert$. Conversely, if both coordinates are non-negative, the element $\Xi=\sqrt{Q_+}\,\Pi_++\sqrt{Q_-}\,\Pi_-$ is real, and $\Xi^2=Q$.

The image is closed under multiplication and under addition, it is convex, and it is pointed: it is a cone in the strict sense. Its two boundary rays are $\mathbb{R}_{\ge0}\Pi_+$ and $\mathbb{R}_{\ge0}\Pi_-$, and its apex is the origin.

### The Image Is the Cone and Not the Plane

The square map is not onto. The element $-1$ has no square root, since a square has $q\ge\lvert q'\rvert$ and $-1$ has $q=-1$; more generally no element outside the forward cone is a square, and the cone is a proper subset of the plane with non-empty interior. Over $\mathbb{C}$ the same map is onto, and the difference is exactly the difference between a field and a ring with two idempotents: the squaring of each coordinate is onto over $\mathbb{C}$ because every complex number has a square root, and it is onto $\mathbb{R}_{\ge0}$ over $\mathbb{R}$.

### The Counts of the Fibres

The fibres are read off the idempotent coordinates at once, since $\Xi_\pm^2=Q_\pm$ has two solutions $\pm\sqrt{Q_\pm}$ when $Q_\pm>0$, the single solution $0$ when $Q_\pm=0$, and none when $Q_\pm<0$.

| The value $Q$ | The fibre $\sigma^{-1}(Q)$ | The count |
|---|---|---|
| interior of the cone, $Q_+>0$ and $Q_->0$ | the four sign choices $(\pm\sqrt{Q_+},\pm\sqrt{Q_-})$ | $4$ |
| boundary minus the origin, one coordinate zero | the two sign choices on the other coordinate | $2$ |
| the origin | the origin | $1$ |
| outside the cone, one coordinate negative | empty | $0$ |

The table is the count of the roots of *Square Roots of a General Element in the Split-Complex Algebra*, and it is the table of the cardinalities $4,2,1,0$ of the corpus. Over $\mathbb{C}$ the corresponding table has two entries, two for a non-zero value and one for zero, and the two tables differ at both ends: four where the complex case has two, and nothing where the complex case always has something.

## The Derivative

### The Multiplication by $2Q$

**Proposition.** The map is differentiable, and its differential at $Q$ is the multiplication by $2Q$:

$$
D\sigma(Q)(X)=QX+XQ=2QX .
$$

**Proof.** $(Q+X)^2=Q^2+QX+XQ+X^2$ and the last term is of second order in $X$; the ring is commutative, so the two linear terms coincide.

The differential is therefore not an arbitrary linear map but a multiplication, and the linear map $X\mapsto 2QX$ has the matrix

$$
\begin{pmatrix}2q&2q'\\2q'&2q\end{pmatrix}
$$

in the basis $1,j$: a multiplication in the split-complex algebra, with equal diagonal entries and equal off-diagonal entries.

### The Jacobian

**Proposition.** The Jacobian determinant is

$$
J_\sigma(Q)=\det\bigl(2Q\cdot\bigr)=4(q^2-q'^2)=4N(Q) .
$$

**Proof.** The determinant of the displayed matrix is $4q^2-4q'^2$. It is also the product of the two eigenvalues $2Q_+$ and $2Q_-$ of the multiplication, that is $4Q_+Q_-=4N(Q)$.

The Jacobian is the split norm up to the factor four, so it is positive inside the double cone, negative outside it, and zero exactly on the pair of null lines.

### The Critical Set

**Theorem.** The critical set of the square map is the union of the two null lines,

$$
\{Q : J_\sigma(Q)=0\}=\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_- ,
$$

and the map is a local diffeomorphism at every other point.

**Proof.** $J_\sigma(Q)=4Q_+Q_-$ vanishes exactly when one idempotent coordinate vanishes, which is $Q\in\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$. Off that set the differential is invertible and the inverse function theorem applies.

The critical set is the set of zero divisors with the origin adjoined, which is *Zero Divisors of the Split-Complex Algebra*; a multiplication is singular exactly at the elements that annihilate something, and the square map inherits its singular set from the multiplication.

## The Local Structure

### The Two Sheets over the Interior

Over the interior of the forward cone the map is four-to-one, and the four preimages fall into two pairs under the sign change $\Xi\mapsto-\Xi$. The two pairs are the two **sheets**, and each is a region of the source:

$$
\{\Xi : N(\Xi)>0\}\ \text{and}\ \{\Xi : N(\Xi)<0\} ,
$$

the timelike and the spacelike region of the plane of the preimages.

**Proof.** The first pair of roots has $N(\Xi)=\Xi_+\Xi_-=\sqrt{Q_+Q_-}>0$ and the second has the opposite sign, so the two pairs lie in the two regions, and the sign change keeps each pair in its region. Both regions are mapped onto the interior of the cone, since $N(\Xi^2)=N(\Xi)^2>0$ and every interior value has the two roots.

So the square map folds the two regions of the source onto one region of the target, two-to-one on each, and the folding is the identification of $\Xi$ with $-\Xi$.

### The Boundary

Over the boundary of the cone minus the origin the map is two-to-one, the two preimages lying on the null lines of the source and being opposite to each other. The boundary is the image of the null lines, and on it the differential has rank one: the boundary is the fold set.

### The Branch Locus

**Theorem.** The image of the critical set is the pair of null rays, that is the boundary of the image cone.

**Proof.** A null element is $\Xi=t\Pi_+$ or $\Xi=t\Pi_-$ with real $t$, and its square is $t^2\Pi_+$ or $t^2\Pi_-$, on the boundary. Conversely every boundary point $s\Pi_+$ with $s\ge0$ is the square of $\pm\sqrt{s}\,\Pi_+$.

The **branch locus** of the map is therefore the boundary of the cone, and it is where the two sheets meet: the four branches collapse pairwise as the value crosses the boundary, from four to two, and to one at the apex. This is the geometric content of the table of fibres.

## The Four Inverse Branches

### The Branches

On the interior of the cone the map has four single-valued inverses, one for each sign choice:

$$
\Xi_{\epsilon_+\epsilon_-}=\epsilon_+\sqrt{Q_+}\,\Pi_++\epsilon_-\sqrt{Q_-}\,\Pi_- , \qquad \epsilon_\pm\in\{+1,-1\} .
$$

Each is a smooth function of $Q$ on the interior, and the four exhaust the fibre. The interior of the cone is convex, hence simply connected, so the four-valued inverse has no monodromy: the branches are global, and there is no need of a cut plane as there is for the complex square root.

### The Identification with the Roots

The four branches are the four roots of *Square Roots of a General Element in the Split-Complex Algebra*, in the order of the two signs. The article there counts them; this article identifies them with the local inverses of a differentiable map, and the identification is the statement that the algebraic count and the differential count agree: four on the interior, two on the boundary minus the origin, one at the origin, none outside.

## The Comparison with the Complex Case

### The Square Is Not Onto

Over $\mathbb{C}$ the map $z\mapsto z^2$ is onto, and the equation $z^2=w$ has two solutions for every $w\neq0$ and one for $w=0$. Here the map is onto the forward cone and no further, and its fibres have four, two, one and no points. The obstruction is the ring and not the map: the squaring of the idempotent coordinates is the squaring of $\mathbb{R}$, which is onto $\mathbb{R}_{\ge0}$, and the transport back gives a cone where the complex case gives the plane.

### One Critical Point There

Over $\mathbb{C}$ the differential of $z\mapsto z^2$ is the multiplication by $2z$, invertible for every $z\neq0$, so the critical set is the origin alone. Here the critical set is the pair of null lines: the multiplication by $2Q$ is singular exactly when $2Q$ is a zero divisor. The two critical sets are the two faces of one fact, that the multiplication by a non-zero element of $\mathbb{C}$ is always injective and the multiplication by a zero divisor of $\mathbb{C}_{\mathrm{spl}}$ never is.

### The Counts Compared

| The value | Over $\mathbb{C}$ | Over $\mathbb{C}_{\mathrm{spl}}$ |
|---|---|---|
| interior of the image | $2$ | $4$ |
| boundary of the image, off the apex | $2$ | $2$ |
| the apex | $1$ | $1$ |
| outside the image | — | $0$ |

The complex image is the whole plane, so it has no outside; the split image is a cone, so it has one. The count of two at every non-zero complex value becomes the count of four on the interior and of zero outside, and the change of count is the change of the image.

## Summary

The square map of the split-complex space has the image the forward cone $q\ge\lvert q'\rvert$, and it is not onto: $-1$ is not a square, and no element outside the cone is. Its differential at $Q$ is the multiplication by $2Q$, of Jacobian determinant $4(q^2-q'^2)=4N(Q)$, so the critical set is the pair of null lines and the map is a local diffeomorphism everywhere else.

The fibres have four points on the interior of the cone, two on its boundary minus the origin, one at the origin and none outside; the four preimages of an interior value fall into the two sheets $N(\Xi)>0$ and $N(\Xi)<0$, each mapped two-to-one onto the interior, and the two sheets meet on the null lines, which are the branch locus. The four branches are the four roots, global on the interior because that region is simply connected.

Over $\mathbb{C}$ the square is onto and its only critical point is the origin; over $\mathbb{C}_{\mathrm{spl}}$ the image is a cone whose boundary is the image of the critical set. Both differences come from one fact: the multiplication by a non-zero element of the split ring need not be injective, and it fails exactly on the null lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(Q)=Q^2$ | The square map |
| $\sigma(q,q')=(q^2+q'^2,2qq')$ | The square map on the coordinates |
| $\sigma(Q)_\pm=Q_\pm^2$ | The square map in idempotent coordinates |
| $\mathcal{C}_+=\{q\ge\lvert q'\rvert\}$ | The forward cone, the image |
| $D\sigma(Q)=2Q\cdot$ | The differential, the multiplication by $2Q$ |
| $J_\sigma(Q)=4(q^2-q'^2)=4N(Q)$ | The Jacobian determinant |
| $\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$ | The critical set and the branch locus of the image |
| $\Xi_{\epsilon_+\epsilon_-}$ | The four inverse branches |

## Further Reading

- John W. Milnor, *Topology from the Differentiable Viewpoint* (Princeton University Press, 2nd ed. 1997), for regular values, the inverse function theorem and the count of preimages.
- Morris W. Hirsch, *Differential Topology* (Springer, Graduate Texts in Mathematics 33, 1976), for the rank of a differentiable map and the structure of its critical set.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the squaring map of the split plane and its cone.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the square map of a Clifford algebra and its degenerate fibres.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the reduction of a squaring to the idempotent coordinates.
