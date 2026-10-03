
# __Complex Topology__

## Introduction

This article collects the topology of the complex algebra $\mathbb{C}$ as a space and of its group of units. It uses the algebra and the two distinguished subspaces of *Complex Algebra* and *Complex Subspaces*, the norm $N(A) = A\bar{A} = |A|^2$ and the invertibility criterion of *Complex Norm and Invertibility*, and the Lie-group structure and exponential of *Complex Exponential and Lie Group Structure*. No physics is invoked and no new result is claimed.

The complex case is the simplest in the family and the whole of its topology is the topology of the plane and the circle. The algebra itself is $\mathbb{R}^2$, hence contractible; the group of units is the punctured plane, homotopy equivalent to the unit circle, with fundamental group $\mathbb{Z}$. The biquaternion algebra has a much richer topology, with the Euclidean sphere $S^7$, the null cone and its link; none of those objects exists here, and their absence is the definiteness of the norm and the emptiness of the zero-divisor class. The group structure of the units and their connectedness are the subject of the companion article *Complex Exponential and Lie Group Structure*; this article owns the ambient space and its distinguished subsets, the unit circle and its homotopy, and the punctured plane.

**Conventions.** The basis is $1$, $i$ with $i^2 = -1$; a complex number is $A = a+i a'$ with real coordinates $(a,a')$; the norm is $N(A) = a^2+a'^2$ and the Euclidean norm is $|A| = \sqrt{N(A)} = \sqrt{a^2+a'^2}$; the group of units is $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$.

## The Algebra as a Topological Space

The map

$$
A = a+i a' \longmapsto (a,a')
$$

is a linear isometry of $(\mathbb{C}, |\cdot|)$ onto the Euclidean plane $\mathbb{R}^2$. The topology of $\mathbb{C}$ is therefore the Euclidean topology of $\mathbb{R}^2$; multiplication is bilinear, hence continuous, so $\mathbb{C}$ is a topological algebra over $\mathbb{R}$; and inversion is continuous on the units, so $\mathbb{C}^\times$ is a topological group.

**Theorem (contractibility).** $\mathbb{C}$ is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{C}) = 0$ for all $n \ge 1$.

**Proof.** The straight-line homotopy

$$
H(t, A) = (1-t) A, \qquad t \in [0,1],
$$

is continuous with $H(0,A) = A$ and $H(1,A) = 0$, so the identity is homotopic to the constant map at $0$.

Thus every map into $\mathbb{C}$ is null-homotopic, and the same homotopy contracts each of the two distinguished subspaces, since both are closed under scalar multiplication:

$$
\mathbb{R}_{\mathbb{C}} \cong \mathbb{R}, \qquad i\mathbb{R}_{\mathbb{C}} \cong \mathbb{R}.
$$

The two subspaces carry no topology beyond that of the line; the content on the norm of *Complex Subspaces* lies in the quadratic form restricted to them, not in their topology. In the biquaternion case the fixed and anti-fixed spaces of the corresponding involution are the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}} \cong \mathbb{R}^4$ and $i\mathbb{H}_{\mathbb{B}} \cong \mathbb{R}^4$, also contractible; the complex case is the same statement in the lowest dimension.

## The Unit Circle

**Definition.** The **unit circle** is

$$
S^1 = \{A \in \mathbb{C} : |A| = 1\} = \{A : N(A) = 1\} = U(1).
$$

This is where the complex case departs from the biquaternion one in the most useful way. For the biquaternion algebra the Euclidean unit sphere $\|\tilde{Q}\|_E = 1$ is a genuine sphere $S^7$ but is not a group, because the Euclidean norm is not multiplicative and the sphere contains zero divisors; the level set that is a group, $N = 1$, is a different, non-compact object. Here the two level sets coincide,

$$
\{A : |A| = 1\} = \{A : N(A) = 1\},
$$

because the norm is positive definite and equals the square of the Euclidean norm. The unit sphere is therefore a **group**:

**Proposition.** $S^1 = U(1)$ is a compact, connected, abelian topological group whose underlying space is a manifold of dimension $1$, isomorphic to $SO(2)$ and to $\mathbb{R}/2\pi\mathbb{Z}$.

**Proof.** It is the kernel of the norm on $\mathbb{C}^\times$, hence a subgroup; it is closed and bounded in $\mathbb{C} \cong \mathbb{R}^2$, hence compact; the parametrisation $t \mapsto e^{it}$ exhibits it as the continuous image of the connected group $\mathbb{R}$ with kernel $2\pi\mathbb{Z}$, so it is connected and isomorphic to $\mathbb{R}/2\pi\mathbb{Z}$; and it acts on the plane by rotations, giving $U(1) \cong SO(2)$.

The compactness is exactly the multiplicativity of the complex norm that fails for the biquaternion semi-norm: the unit sphere is a group because $|AB| = |A||B|$ and the definite form makes the level set bounded. This is the base case of the theorem that the unit sphere of a normed division algebra with associative multiplication carries a Lie-group structure; the smooth structure that structure needs is the subject of the companion article *Complex Exponential and Lie Group Structure*, and only the group and its topology are used here. The cases are $S^0$, $S^1$, $S^3$, the finite list of spheres that carry such a structure, and $S^1$ is the complex member.

## The Group of Units

The **group of units** is

$$
\mathbb{C}^\times = \{A : N(A) \neq 0\} = \mathbb{C} \setminus \{0\},
$$

the **punctured plane**, a topological group whose underlying space is a manifold of real dimension $2$, open and dense in $\mathbb{C}$, connected and non-compact.

**Theorem (homotopy type).** The map

$$
\pi : \mathbb{C}^\times \longrightarrow S^1, \qquad \pi(A) = \frac{A}{|A|},
$$

is a continuous retraction, and $\mathbb{C}^\times$ deformation retracts onto $S^1$. Consequently

$$
\mathbb{C}^\times \simeq S^1, \qquad \pi_1(\mathbb{C}^\times) \cong \mathbb{Z}, \qquad \pi_n(\mathbb{C}^\times) = 0 \ \ (n \ge 2).
$$

**Proof.** The polar splitting of *Complex Norm and Invertibility* gives a homeomorphism

$$
\mathbb{C}^\times \longrightarrow \mathbb{R}_{>0} \times S^1, \qquad A \longmapsto (|A|, A/|A|),
$$

with inverse $(r,u) \mapsto ru$. The first factor $\mathbb{R}_{>0}$ is contractible, so the product deformation retracts onto $\{1\} \times S^1 \cong S^1$ by the homotopy $((r,u),t) \mapsto (r^{1-t}, u)$; equivalently the map $\pi$ is a retraction and $H(t,A) = A/|A|^{\,t}$ deforms the identity to $\pi$. The homotopy groups of $S^1$ are $\pi_1 \cong \mathbb{Z}$ and $\pi_n = 0$ for $n \ge 2$, and homotopy equivalences preserve these.

The generator of $\pi_1(\mathbb{C}^\times)$ is the class of the loop

$$
\gamma(t) = e^{2\pi i t}, \qquad t \in [0,1],
$$

traversed once round the circle; the integer attached to a closed loop is its **winding number** about the origin, and the identification $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$ is the statement that the winding number classifies loops up to homotopy. This is the topological form of the argument principle of *Complex Analysis*, and it is why the contour integral $\oint dA/A = 2\pi i$ is the nontrivial residue. In the biquaternion case the unit group $\mathbb{B}^\times \cong GL(2,\mathbb{C})$ deformation retracts onto the maximal compact subgroup $U(2) \cong S^1 \times S^3$, of real dimension $4$, with $\pi_1 \cong \mathbb{Z}$ and, additionally, $\pi_3 \cong \mathbb{Z}$; the circle here is the first factor of that product with the three-sphere removed.

## The Punctured Plane and Its Fundamental Group

The punctured plane is the group of units, and it is the standard example of a space that is connected but not simply connected.

- **Path-connected.** Every $A \neq 0$ joins to the circle by the rescaling $t \mapsto A/|A|^{\,t}$, and any two points of the circle join by an arc; the concatenation is a path from $A$ to $1$ through nonzero elements.
- **Not simply connected.** The loop $\gamma(t) = e^{2\pi i t}$ is not null-homotopic, its winding number being $1 \neq 0$; equivalently there is no continuous branch of the argument $\arg : \mathbb{C}^\times \to \mathbb{R}$.
- **Universal cover.** The map

$$
p : \mathbb{R} \times \mathbb{R}_{>0} \longrightarrow \mathbb{C}^\times, \qquad p(\theta, r) = r e^{i\theta},
$$

is a homeomorphism onto $\mathbb{C}^\times$ after the identification $(\theta + 2\pi, r) \sim (\theta, r)$; equivalently the exponential $\exp : \mathbb{C} \to \mathbb{C}^\times$ is a universal covering map of $\mathbb{C}^\times$, with deck transformation group the kernel $2\pi i\,\mathbb{Z}$ generated by $A \mapsto A + 2\pi i$. The **universal cover** of $\mathbb{C}^\times$ is therefore contractible, being a half-plane product, and the covering is the universal one because $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$ acts freely and transitively on the fibres. This is the logarithmic-coordinate picture of *Complex Exponential and Lie Group Structure* read topologically.

## The Boundary of the Polar Representation

The polar parametrisation of the group of units,

$$
\Phi : \mathbb{R}_{>0} \times \mathbb{R} \longrightarrow \mathbb{C}^\times, \qquad \Phi(r, \theta) = r e^{i\theta},
$$

is a surjective local homeomorphism that is not injective: $\Phi(r, \theta) = \Phi(r, \theta + 2\pi k)$ and only these identifications occur. After the quotient by $2\pi\mathbb{Z}$ in the angular variable it descends to a homeomorphism $\mathbb{R}_{>0} \times (\mathbb{R}/2\pi\mathbb{Z}) \to \mathbb{C}^\times$, and its image is all of $\mathbb{C}^\times$.

**There is no boundary of the polar representation in the complex case.** The parametrisation fails to cover exactly the complement $\mathbb{C} \setminus \mathbb{C}^\times = \{0\}$, which is a single point, not a hypersurface, and the circle $S^1$ is compact so the angular variable has no boundary either. In the biquaternion algebra the polar parametrisation fails on the null cone, a real algebraic variety of real dimension $6$, which is the genuine boundary of the polar representation and carries the link $L = \mathcal{N} \cap S^7_E$; the complex case has no such set, because the norm is definite and the zero-divisor class is empty. The absent null cone and the absent link are the mathematical content of the definiteness of $\mathbb{C}$.

**The one-point compactification.** If a single point $\infty$ is adjoined to $\mathbb{C}$, the resulting compact space is a two-sphere,

$$
\mathbb{C} \cup \{\infty\} \cong S^2,
$$

the **Riemann sphere**, and $\mathbb{C}^\times$ becomes the sphere with two points removed, $\mathbb{C}^\times \cong S^2 \setminus \{0,\infty\}$, a cylinder. The point $\infty$ is the topological completion of the unbounded direction of the plane; it is a single point, not the many-pointed boundary that the indefinite form would produce, and the companion article *Complex Analysis* develops the function theory on it. The sphere is the best compact model of $\mathbb{C}$; there is no compact model underlying the group structure of $\mathbb{C}^\times$, which is non-compact and only has the circle as its compact core.

## Comparison with the Topology of the Biquaternion Algebra

| Structure | $\mathbb{C}$ | $\mathbb{B}$ |
|---|---|---|
| Algebra as a space | $\mathbb{R}^2$, contractible | $\mathbb{R}^8$, contractible |
| Euclidean unit sphere | $S^1$, a group $U(1)$ | $S^7$, not a group |
| Norm-one level set | $S^1 = U(1)$, compact | $SL(2,\mathbb{C})$, non-compact |
| Null cone $\{N = 0\}$ | $\{0\}$, a point | real dimension $6$, the cone on its link |
| Link of the null cone | none | $S^1$-bundle over $S^2 \times S^2$, $\pi_2 \cong \mathbb{Z}$ |
| Group of units | $\mathbb{C}^\times \simeq S^1$, $\pi_1 \cong \mathbb{Z}$ | $\mathbb{B}^\times \simeq U(2) \simeq S^1 \times S^3$, $\pi_1 \cong \mathbb{Z}$, $\pi_3 \cong \mathbb{Z}$ |
| Compact core | $S^1$, dimension $1$ | $U(2)$, dimension $4$ |

The two algebras share the contractibility of the ambient space and the vanishing of the second homotopy group of the units, and they share a factor $S^1$ in the group of units. They differ in everything else: the complex algebra has a compact unit sphere that is a group, no null cone and no link, and a group of units that is a product of a line and a circle, whereas the biquaternion algebra has a non-group unit sphere, a six-dimensional null cone with a five-dimensional link, and a group of units with an extra three-sphere factor. Each difference traces to a single cause: the norm of $\mathbb{C}$ is real and definite, that of $\mathbb{B}$ is complex and indefinite.

## Summary

The complex algebra $\mathbb{C} \cong \mathbb{R}^2$ is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{C}) = 0$ for all $n \ge 1$; the two distinguished subspaces are contractible copies of the line. The unit circle $S^1 = \{|A| = 1\} = \{N(A) = 1\}$ is a compact, connected, abelian topological group isomorphic to $U(1) \cong SO(2) \cong \mathbb{R}/2\pi\mathbb{Z}$; it is a group because the norm is definite and multiplicative, so that the Euclidean unit sphere and the norm-one level set coincide.

The group of units is the punctured plane $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$, a connected, non-compact topological group whose underlying space is a manifold of real dimension $2$, which deformation retracts onto $S^1$ by $A \mapsto A/|A|$. Hence $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$, generated by $t \mapsto e^{2\pi i t}$ with the winding number as its invariant, and $\pi_n(\mathbb{C}^\times) = 0$ for $n \ge 2$; the universal cover is contractible and the covering is $\exp$. The polar parametrisation covers all of $\mathbb{C}^\times$ up to the identification $\theta \sim \theta + 2\pi$, and it has **no boundary**, since the only non-polar point is the single origin and the angular circle is compact. There is no null cone and no link, because the norm is definite and the zero-divisor class is empty; the only distinguished subset beside the unit circle is the one-point compactification $\mathbb{C} \cup \{\infty\} \cong S^2$. Compared with the biquaternion algebra, the complex case loses the seven-sphere, the null cone and its link, and the three-sphere factor of the unit group, and keeps a compact unit circle that is a group.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C} \cong \mathbb{R}^2$ | the complex algebra as a topological space; contractible |
| $A = a+i a'$ | a complex number with real coordinates $(a,a')$ |
| $N(A) = a^2+a'^2$ | the norm; definite, $N = |A|^2$ |
| $|A| = \sqrt{N(A)}$ | the Euclidean norm and modulus |
| $S^1 = U(1) = \{A : N(A) = 1\}$ | the unit circle, a compact topological group, $\cong SO(2) \cong \mathbb{R}/2\pi\mathbb{Z}$ |
| $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ | the group of units, the punctured plane; $\simeq S^1$ |
| $\pi(A) = A/|A|$ | the retraction; $H(t,A) = A/|A|^{\,t}$ the deformation retraction |
| $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$ | the fundamental group, the winding number |
| $\Phi(r,\theta) = re^{i\theta}$ | the polar parametrisation, covering $\mathbb{C}^\times$ |
| $\mathbb{C} \cup \{\infty\} \cong S^2$ | the one-point compactification, the Riemann sphere |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | real and imaginary subspaces, contractible lines |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the fundamental group, covering spaces and homotopy equivalences.
- James R. Munkres, *Topology*, 2nd edition (Prentice Hall, 2000), for the Euclidean topology of the plane and the punctured plane.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the winding number, the argument principle and the Riemann sphere.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the geometric topology of the circle and the plane.
- Frank B. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, Graduate Texts in Mathematics 94, 1983), for the topology of Lie groups and maximal compact subgroups.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the sphere and unit-group topology of the higher-dimensional relatives.
