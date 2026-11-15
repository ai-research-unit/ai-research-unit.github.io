# __The Homotopy of $\mathrm{GL}_n(\mathbb{R})$ and of $\mathrm{SO}(n)$__

## Introduction

**The general linear group over $\mathbb{R}$ has the homotopy type of the orthogonal group, so all of its topology is the topology of the compact form, and the noncompact directions contribute nothing.**

The article proves the polar decomposition as a deformation retraction, deduces that $\mathrm{GL}_n(\mathbb{R})$ is homotopy equivalent to $\mathrm{O}(n)$ and that its two components are each homotopy equivalent to $\mathrm{SO}(n)$, computes $\pi_0,\pi_1,\pi_2$ for small $n$ from the fibrations $\mathrm{SO}(n)\to S^{n-1}$ and $\mathrm{SO}(n)\to\mathrm{SO}(n)/\mathrm{SO}(n-1)$, identifies $\mathrm{SO}(3)$ with $\mathbb{RP}^{3}$ and $\mathrm{SO}(4)$ with $(S^{3}\times S^{3})/(\mathbb{Z}/2)$, and states the Bott periodicity result that stops the pattern at $n=5$. It assumes *The Topology of $M_n(\mathbb{R})$ and the Sign of the Determinant* and *The Polar Decomposition from the Two Halves and the Sign of the Determinant*. It defers the cone and the analysis to *The Positive Cone and Its Boundary*.

## The Deformation Retraction

**Theorem.** $\mathrm{O}(n)$ is a strong deformation retract of $\mathrm{GL}_n(\mathbb{R})$, and $\mathrm{SO}(n)$ is a strong deformation retract of $\mathrm{GL}_n(\mathbb{R})^{+}$.

*Proof.* Write $A=QP$ with $Q\in\mathrm{O}(n)$ and $P$ symmetric positive definite. For $t\in[0,1]$ put $P_t=P^{t}$, the positive power defined by the spectral theorem, and $A_t=QP_t$. Then $A_0=Q$, $A_1=A$, and each $A_t$ is invertible with $A_t^{\mathsf T}A_t=P_t^{2}$, so $A_t\in\mathrm{GL}_n(\mathbb{R})$. The map $(A,t)\mapsto A_t$ is continuous in $(A,t)$ because $P_t$ is, and it fixes every orthogonal matrix. The determinant is $\det Q\cdot\det P_t>0$, so the retraction respects the two components.

**The retraction is the same as the polar decomposition run backwards.** The path $t\mapsto A_t$ removes the stretch continuously and leaves the rotation. In the language of *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{R})$* it is the geodesic from $A$ to $K$ in the symmetric space.

**Consequence.** The inclusions $\mathrm{O}(n)\subset\mathrm{GL}_n(\mathbb{R})$ and $\mathrm{SO}(n)\subset\mathrm{GL}_n(\mathbb{R})^{+}$ induce isomorphisms on every homotopy group, and the two spaces have the same homology and cohomology. So nothing about $\mathrm{GL}_n(\mathbb{R})$ needs to be computed in the noncompact group.

**The same argument works with the transpose on the other side.** Writing $A=P'Q'$ with $P'$ positive definite gives the retraction $A\mapsto P_t'Q'$, and the two retractions are homotopic.

## The Two Components

**$\mathrm{GL}_n(\mathbb{R})$ has exactly two components, and each is homotopy equivalent to $\mathrm{SO}(n)$.** The determinant is a continuous surjection onto $\mathbb{R}^{\times}$, so there are at least two components. The retraction of the previous section shows that each component retracts onto a component of $\mathrm{O}(n)$, and $\mathrm{O}(n)$ has exactly two components, cut by the determinant. Hence

$$
\mathrm{GL}_n(\mathbb{R})\simeq\mathrm{O}(n)=\mathrm{SO}(n)\sqcup(-\mathrm{I})\,\mathrm{SO}(n).
$$

The second component is a copy of the first, translated by any orthogonal matrix of determinant $-1$, for instance $\operatorname{diag}(-1,1,\dots,1)$.

**The two components are homeomorphic and the homeomorphism is a group automorphism up to a sign.** Multiplication by $\operatorname{diag}(-1,1,\dots,1)$ is a homeomorphism of one component onto the other, and it is not an inner automorphism; it is conjugation by a matrix of determinant $-1$.

**So the homotopy groups of $\mathrm{GL}_n(\mathbb{R})$ are those of $\mathrm{SO}(n)$, and $\pi_0=\mathbb{Z}/2$.** For $n=1$ the group is $\mathbb{R}^{\times}$, with two contractible components, and $\pi_0=\mathbb{Z}/2$ as well.

## The Fibration over the Sphere

**Theorem.** $\mathrm{SO}(n)$ acts transitively on $S^{n-1}$, and the stabiliser of a unit vector is $\mathrm{SO}(n-1)$. Hence $\mathrm{SO}(n)\to S^{n-1}$ is a fibre bundle with fibre $\mathrm{SO}(n-1)$.

*Proof.* Transitivity: any unit vector is the first column of some orthogonal matrix, and the determinant can be corrected to $+1$ by changing the sign of another column. The stabiliser of $e_1$ consists of the orthogonal matrices fixing $e_1$ and acting orthogonally on $e_1^{\perp}$, that is of $\mathrm{O}(n-1)$, and the determinant condition selects $\mathrm{SO}(n-1)$.

**The long exact sequence of the fibration computes the low homotopy groups by induction.** From $\mathrm{SO}(n-1)\to\mathrm{SO}(n)\to S^{n-1}$ one gets

$$
\pi_k\bigl(\mathrm{SO}(n)\bigr)\cong\pi_k\bigl(\mathrm{SO}(n-1)\bigr)\quad\text{for }k\le n-3,
$$

because $\pi_k(S^{n-1})=0$ in that range. So the homotopy groups of $\mathrm{SO}(n)$ stabilise as $n$ grows, and the stable values are the homotopy groups of the infinite orthogonal group.

**The first two groups.** $\pi_2(S^{n-1})=0$ for $n\ge3$, so $\pi_2(\mathrm{SO}(n))=0$ for every $n\ge3$. $\pi_1(S^{n-1})=0$ for $n\ge3$, so $\pi_1(\mathrm{SO}(n))\cong\pi_1(\mathrm{SO}(n-1))$ for $n\ge4$; together with $\pi_1(\mathrm{SO}(3))=\mathbb{Z}/2$ this gives

$$
\pi_1\bigl(\mathrm{SO}(n)\bigr)=\mathbb{Z}/2\quad(n\ge3),\qquad \pi_1\bigl(\mathrm{SO}(2)\bigr)=\mathbb{Z}.
$$

**The third group.** $\pi_3(S^{3})=\mathbb{Z}$, and the segment $\pi_3(\mathrm{SO}(4))\to\pi_3(S^{3})\to\pi_2(\mathrm{SO}(3))$ with $\pi_2(\mathrm{SO}(3))=0$ shows that $\pi_3(\mathrm{SO}(4))$ contains a $\mathbb{Z}$; the full value is $\mathbb{Z}\oplus\mathbb{Z}$, matching the double cover $S^{3}\times S^{3}$.

**A table of the low groups.**

| $n$ | $\pi_1(\mathrm{SO}(n))$ | $\pi_2$ | $\pi_3$ |
|---|---|---|---|
| $2$ | $\mathbb{Z}$ | $0$ | $0$ |
| $3$ | $\mathbb{Z}/2$ | $0$ | $\mathbb{Z}$ |
| $4$ | $\mathbb{Z}/2$ | $0$ | $\mathbb{Z}\oplus\mathbb{Z}$ |

The entries for $n=2$ follow from $\mathrm{SO}(2)=S^{1}$; those for $n\ge5$ agree with $n=4$ in these three degrees because of the stabilisation range.

## The Two Model Spaces

**$\mathrm{SO}(3)$ is the real projective space $\mathbb{RP}^{3}$.** The unit quaternions form $S^{3}$, and conjugation by a unit quaternion is a rotation of the imaginary quaternions, which are $\mathbb{R}^{3}$; the map $S^{3}\to\mathrm{SO}(3)$ is a surjective group homomorphism with kernel $\{\pm1\}$. Hence $\mathrm{SO}(3)\cong S^{3}/\{\pm1\}=\mathbb{RP}^{3}$, with $\pi_1=\mathbb{Z}/2$ and $\pi_3=\mathbb{Z}$.

**$\mathrm{SO}(4)$ is $(S^{3}\times S^{3})/(\mathbb{Z}/2)$.** Identify $\mathbb{R}^{4}$ with the quaternions and let $S^{3}\times S^{3}$ act by $(u,v)\cdot x=uxv^{-1}$. The kernel of the action is $\{(1,1),(-1,-1)\}$, so $\mathrm{SO}(4)\cong(S^{3}\times S^{3})/(\mathbb{Z}/2)$, and correspondingly $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$.

**The two models explain the exceptional behaviour at $n=4$.** For $n\ge5$ the group $\mathrm{SO}(n)$ is simple; at $n=4$ it is not, because of the two quaternionic factors. At $n=3$ it is simple but not simply connected. The two facts are the two exceptional cases of the general theorem that $\mathrm{SO}(n)$ is simple for $n\ge3$ and $n\ne4$.

**The identifications are verified by the dimension and the cover.** $\dim\mathrm{SO}(3)=3=\dim\mathbb{RP}^{3}$ and $\dim\mathrm{SO}(4)=6=\dim(S^{3}\times S^{3})$, and in both cases the covering map has degree two with kernel of order two, matching $\pi_1=\mathbb{Z}/2$.

## What Happens at $n=2$

**$\mathrm{SO}(2)$ is the circle, so its topology is the topology of $\mathbb{Z}$.** The group is

$$
\mathrm{SO}(2)=\left\{\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}\right\},
$$

homeomorphic to $S^{1}$ by $\theta\mapsto$ the matrix, with $\pi_1=\mathbb{Z}$ and all higher homotopy groups zero.

**Consequently $\mathrm{GL}_2(\mathbb{R})^{+}$ has fundamental group $\mathbb{Z}$.** The retraction onto $\mathrm{SO}(2)$ gives the isomorphism, and the generator is the loop $t\mapsto$ rotation by $2\pi t$. This is the one dimension in which the fundamental group of the positive component is infinite.

**The loop is detected by the angle of the rotation, not by the matrix.** The path returns to the identity at $t=1$, but the rotation angle has advanced by $2\pi$; this is the same phenomenon that makes the exponential not injective, and it is the reason $\mathrm{SO}(2)\to\mathrm{SO}(2)$, $\theta\mapsto2\theta$, is a covering of degree two.

**At $n\ge3$ the loop becomes contractible as a loop in the bigger group.** The rotation in a plane can be deformed, inside $\mathrm{SO}(n)$, to a rotation in another plane and then undone; the obstruction reduces to $\mathbb{Z}/2$, and the surviving element is the path that reverses the orientation of a plane twice.

## Why the Pattern Stops

**Bott periodicity: the stable homotopy of $\mathrm{SO}$ is periodic with period eight.** For $k\le n-2$ the group $\pi_k(\mathrm{SO}(n))$ depends only on $k$, and the stable values are

$$
\mathbb{Z}/2,\ \mathbb{Z}/2,\ 0,\ \mathbb{Z},\ 0,\ 0,\ 0,\ \mathbb{Z}
$$

for $k=0,1,2,3,4,5,6,7$ and then repeat with period eight. So the induction of the previous sections cannot be continued past $k\approx n$: the groups do not stabilise to a simple answer but to a periodic one.

**The real meaning is that the orthogonal group is the stable object, not the single $\mathrm{SO}(n)$.** The sequence $\mathrm{SO}(1)\subset\mathrm{SO}(2)\subset\cdots$ has a homotopy limit $\mathrm{SO}$, and the periodicity is a statement about that limit. For a fixed $n$ the low groups are the stable ones and the high groups are not.

**The unstable range is where the real geometry lives.** The class in $\pi_{n-1}(\mathrm{SO}(n))$ that generates is the class of the identity map of $S^{n-1}$ seen through the action on the sphere, and it is not stable: it disappears when $n$ increases. This is the homotopy form of the statement that the rotation group acts on the sphere of its own dimension.

## Summary

$\mathrm{O}(n)$ is a strong deformation retract of $\mathrm{GL}_n(\mathbb{R})$ and $\mathrm{SO}(n)$ of $\mathrm{GL}_n(\mathbb{R})^{+}$, so the topology of the general linear group is the topology of the orthogonal group and $\pi_0=\mathbb{Z}/2$. The fibrations $\mathrm{SO}(n)\to S^{n-1}$ with fibre $\mathrm{SO}(n-1)$ give $\pi_2=0$ for $n\ge3$ and $\pi_1=\mathbb{Z}/2$ for $n\ge3$, while $\pi_1(\mathrm{SO}(2))=\mathbb{Z}$. The models $\mathrm{SO}(3)=\mathbb{RP}^{3}$ and $\mathrm{SO}(4)=(S^{3}\times S^{3})/(\mathbb{Z}/2)$ explain the two exceptional dimensions. Beyond the stable range the groups are given by Bott periodicity, with period eight.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{GL}_n(\mathbb{R})^{+}$ | the identity component, $\det>0$ |
| $A_t=QP^{t}$ | the retraction path from $A$ to its orthogonal part |
| $\pi_k$ | the $k$-th homotopy group |
| $\mathbb{RP}^{3}$ | the real projective space, homeomorphic to $\mathrm{SO}(3)$ |
| $S^{3}\times S^{3}/(\mathbb{Z}/2)$ | the model of $\mathrm{SO}(4)$ |
| $\mathrm{SO}$ | the stable orthogonal group, the homotopy limit |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge, 2002), for fibrations, the long exact sequence and the homotopy of classical groups.
- Mimura Mamoru and Hirosi Toda, *Topology of Lie Groups* (American Mathematical Society, 1991), for the homotopy groups of the classical groups in the unstable range.
- [The Topology of $M_n(\mathbb{R})$ and the Sign of the Determinant](the-topology-of-mnr-and-the-sign-of-the-determinant.html), for the two components and the singular set.
- [The Polar Decomposition from the Two Halves and the Sign of the Determinant](the-polar-decomposition-from-the-two-halves-and-the-sign-of-the-determinant.html), for the retraction used here.
- [Homotopy Groups and Fibrations](homotopy-groups-and-fibrations.html), for the long exact sequence used here.
