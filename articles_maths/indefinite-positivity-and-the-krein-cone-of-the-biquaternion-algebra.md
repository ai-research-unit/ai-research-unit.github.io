# __Indefinite Positivity and the Krein Cone of the Biquaternion Algebra__

## Introduction

The dagger is a **positive involution** of the biquaternion algebra: $\mathrm{Sc}(\tilde{Q}^{\dagger}\tilde{Q})=\|\tilde{Q}\|_E^{2}>0$ off zero, and the image of the resulting cone is the Hermitian cone $P=\{\tilde{Q}^{\dagger}\tilde{Q}\}$ of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, the forward light cone of the interval form. The Krein form of the algebra is indefinite, and what replaces that cone is twofold. On the **vectors** there is the set of elements of non-negative Krein square,

$$
P_{K}=\{\tilde{Q}\in\mathbb{B}:[\tilde{Q},\tilde{Q}]\geq0\}=\{\|c\|_E\geq\|v\|_E\},
$$

a cone whose interior is a circle's worth of directions and whose boundary is the Krein null set; on the **operators** there is the $J$-positive cone of the general theory, $\{T=T^{\dagger}:[T\tilde{Q},\tilde{Q}]\geq0\}=J\cdot\{S\geq0\}$, of which the fundamental symmetry $J$ is a member. The first contains the Hermitian cone of the dagger as its future nappe on the Hermitian subspace; the second is the image of the Hilbert positive cone under $J$, a cone of a different kind, which contains $J$ itself and not the identity.

The general theory is *Krein Algebras*, *J-Self-Adjoint and J-Unitary Operators* and *Self-Adjoint Elements and the Positive Cone*; the symmetry is *The Fundamental Symmetry of the Biquaternion Algebra*; the form is *The Biquaternion Krein Form and Its Signature*; the $J$-operators are *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*; and the definite cone, the Cartan involution and the polar decomposition that this article reads indefinitely are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**Conventions.** As throughout: $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$, $[\tilde{Q},\tilde{Q}']=\mathrm{Sc}(\tilde{Q}^{\natural*}\tilde{Q}')$, $\langle\tilde{Q},\tilde{Q}'\rangle=\sum_\mu Q_\mu^{*}Q'_\mu$, $J={}^{\natural}$, and the orthogonal decomposition is the fundamental one, $\tilde{Q}=c+v$ with $c\in\mathbb{C}_{\mathbb{B}}$, $v\in\mathbb{V}_{\mathbb{B}}$, of *The Fundamental Symmetry of the Biquaternion Algebra*.

## The Krein Cone of the Algebra

**Theorem (the cone in the fundamental decomposition).** Write $\tilde{Q}=c+v$ with $c\in\mathbb{C}_{\mathbb{B}}$, $v\in\mathbb{V}_{\mathbb{B}}$. Then

$$
[\tilde{Q},\tilde{Q}]=\|c\|_E^{2}-\|v\|_E^{2},
$$

and

$$
P_{K}=\{\tilde{Q}:[\tilde{Q},\tilde{Q}]\geq0\}=\{\|c\|_E\geq\|v\|_E\},\qquad
P_{K}^{\circ}=\{\|c\|_E>\|v\|_E\},\qquad
\partial P_{K}=\{[\tilde{Q},\tilde{Q}]=0\}.
$$

**Proof.** The two summands are Krein-orthogonal and $[c,c]=\|c\|_E^{2}>0$ on the positive part, $[v,v]=-\|v\|_E^{2}$ on the negative part; the identity follows, and the three characterisations are immediate.

**Theorem (the shape of the cone).** $P_{K}$ is a closed cone with apex at the origin: it is invariant under multiplication by non-negative reals, it is **not** convex when the negative part is nonzero, and it is contractible, being star-shaped with respect to the origin. Its interior is homotopy equivalent to a circle,

$$
P_{K}^{\circ}\simeq S^{1},
$$

and its boundary is the Krein null set, a real cone of dimension $7$.

**Proof.** Homogeneity is $[\lambda\tilde{Q},\lambda\tilde{Q}]=|\lambda|^{2}[\tilde{Q},\tilde{Q}]$ for real $\lambda$; the straight-line homotopy $\tilde{Q}\mapsto t\tilde{Q}$ preserves the inequality, so $P_{K}$ is contractible. To see that it is not convex, take $\tilde{Q}_{1}=e_0+e_2$ and $\tilde{Q}_{2}=-e_0+e_2$: $[\tilde{Q}_{i},\tilde{Q}_{i}]=1-1=0$, both in $P_{K}$, while the midpoint $e_2$ has $[e_2,e_2]=-1<0$. For the interior, the map $\tilde{Q}\mapsto\tilde{Q}/\sqrt{[\tilde{Q},\tilde{Q}]}$ is a deformation retraction of $\{[\tilde{Q},\tilde{Q}]>0\}$ onto $\{[\tilde{Q},\tilde{Q}]=1\}$, and the latter is $\{(c,v):\|c\|_E^{2}-\|v\|_E^{2}=1\}$, in which $c$ runs over a circle of radius $\sqrt{1+\|v\|_E^{2}}$ and $v$ over all of the negative part; it is therefore a product $\simeq S^{1}\times\mathbb{R}^{6}\simeq S^{1}$. The boundary statement is the dimension count of *The Biquaternion Krein Form and Its Signature*.

**Remark (the cone is not an order cone).** $P_{K}$ is a cone in the homogeneous sense but not an order-theoretic one: it is not convex, and it is not pointed, $P_{K}\cap(-P_{K})=\{[\tilde{Q},\tilde{Q}]=0\}\neq\{0\}$. The order that the Krein form defines is the operator order of the next section, not the set of non-negative vectors, exactly as in the general theory (*The Fundamental Symmetry*, §*Remark (the order structure)*).

## The Intersection with the Hermitian Cone

The Hermitian subspace carries two forms of signature $(1,3)$: the biquaternion norm, which equals the Krein form there (*The Biquaternion Krein Form and Its Signature*, §*The Signature*), and the interval form of the definite theory.

**Theorem.** On the Hermitian subspace the Krein cone is the full light cone of the interval form, and its future nappe is the Hermitian cone of the dagger:

$$
P_{K}\cap\mathbb{M}_{+}=\{\tilde{H}\in\mathbb{M}_{+}:N(\tilde{H})\geq0\},
\qquad
P=\{\tilde{Q}^{\dagger}\tilde{Q}:\tilde{Q}\in\mathbb{B}\}=\{\tilde{H}\in\mathbb{M}_{+}:N(\tilde{H})\geq0,\ \mathrm{Sc}(\tilde{H})\geq0\}.
$$

**Proof.** On $\mathbb{M}_{+}$ the Krein square is $N$; an element of the Hermitian subspace is of the form $\tilde{H}=q_0e_0+\sum_k iq'_ke_k$ with $q_0,q'_k$ real, so $N(\tilde{H})=q_0^{2}-\sum_k q'^{2}_k$ and the inequality $N\geq0$ defines the two nappes $q_0\geq|\mathbf{q}'|$ and $q_0\leq-|\mathbf{q}'|$; the Hermitian cone consists of the positive semidefinite Hermitian elements, which are precisely the ones with the additional sign $\mathrm{Sc}(\tilde{H})=q_0\geq0$, and they form one nappe. This is the Hermitian-cone computation of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Cone, the Interval Form and the Isotropic Cone*, read on the Krein form.

**Corollary (the Hermitian cone is inside the Krein cone).** $P\subseteq P_{K}$, and the Krein cone is the union of $P$, its negative $-P$ and the Krein null set inside $\mathbb{M}_{+}$.

**Proof.** The nappe inclusion from the theorem; the remaining nappe is $-P$ because negating an element of $\mathbb{M}_{+}$ negates the scalar part and leaves the vector part, which is the other nappe.

**Remark.** The symmetric difference is genuine: an element of $\mathbb{M}_{+}$ with $q_0^{2}>\sum_kq'^{2}_k$ but $q_0<0$ lies in the Krein cone and not in the Hermitian cone, while an element of the vector subspace with the same square does not lie in either. The two cones are therefore different objects, and the second is not a nappe criterion for the first.

## The $J$-Positive Cone of the Operators

**Definition.** The **$J$-positive cone** is

$$
\mathcal{P}_{J}=\{T:\mathbb{B}\to\mathbb{B}\ \mathbb{C}\text{-linear}:T=T^{\dagger},\ [T\tilde{Q},\tilde{Q}]\geq0\ \forall\tilde{Q}\}.
$$

**Theorem (the cone is the $J$-image of the Hilbert cone).** $T\in\mathcal{P}_{J}$ if and only if $JT$ is self-adjoint and positive for the Hermitian form; hence

$$
\mathcal{P}_{J}=J\cdot\{S:S=S^{*},\ S\geq0\},
$$

the image of the Hilbert positive cone under the fundamental symmetry. In particular $\mathcal{P}_{J}$ is a closed convex cone, stable under sums and under $J$-adjoints; it contains $J=J\cdot e_0$ but not the identity $\mathrm{id}=J\cdot J$, since $J$ is not positive for the Hermitian form.

**Proof.** $[T\tilde{Q},\tilde{Q}]=\langle JT\tilde{Q},\tilde{Q}\rangle$, and $JT$ is self-adjoint exactly when $T$ is $J$-self-adjoint (*J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*, §*The $J$-Adjoint*); the displayed identity is the definition rewritten. Convexity is that of the Hilbert cone transported by the linear bijection $J$. The identity is not in the cone because $J$, which is the definite-obstruction to its positivity, has the negative eigenvalue $-1$.

**Proposition ($J$ is $J$-positive and not Hilbert-positive).** $J\in\mathcal{P}_{J}$, since $[J\tilde{Q},\tilde{Q}]=\|\tilde{Q}\|_E^{2}\geq0$. The Hilbert spectrum of $J$ is the pair $\{+1,-1\}$ with multiplicities $(2,6)$, so $J$ is not positive for the Hermitian form.

**Proof.** The first is the positivity of the fundamental symmetry; the spectrum is the theorem of *The Fundamental Symmetry of the Biquaternion Algebra*.

**Theorem ($J$-projections and the extreme rays).** An idempotent $P$ is $J$-self-adjoint, $P^{\dagger}=P$, if and only if it is the Krein-orthogonal projection onto its range along the Krein-orthogonal complement of that range; equivalently, if and only if $\ker P=(\mathrm{ran}\,P)^{\perp_{K}}$, and the range is then non-degenerate. The definite-orthogonal projections commuting with $J$ — among them the spectral projections $\pi_{\pm}=\tfrac12(\mathrm{id}\pm J)$ of $J$ — are the special case in which the range is definite and definite-orthogonal to its complement; $\pi_{+}$ is the Krein-orthogonal projection onto the centre and is $J$-positive, while $\pi_{-}$ is the Krein-orthogonal projection onto the vector subspace and is $J$-negative. The extreme rays of $\mathcal{P}_{J}$ are the rank-one $J$-projections $J\,|\tilde{Q}\rangle\langle\tilde{Q}|$ with $\|\tilde{Q}\|_E=1$.

**Proof.** If $P^{\dagger}=P$ and $P^{2}=P$ then $[P\tilde{R},\tilde{S}]=[\tilde{R},P\tilde{S}]$; for $\tilde{R}\in\ker P$ this gives $[\tilde{R},\tilde{S}']=0$ for every $\tilde{S}'$ in the range, so $\ker P\subseteq(\mathrm{ran}\,P)^{\perp_{K}}$, and the two sides have the same dimension $\dim\mathbb{B}-\dim\mathrm{ran}\,P$ because the form is non-degenerate, whence equality. Conversely, for the projection $P$ onto a non-degenerate $\mathbb{W}$ along $\mathbb{W}^{\perp_{K}}$, write $\tilde{R}=\tilde{W}+\tilde{T}$ and $\tilde{S}=\tilde{W}'+\tilde{T}'$ with $\tilde{W},\tilde{W}'\in\mathbb{W}$ and $\tilde{T},\tilde{T}'\in\mathbb{W}^{\perp_{K}}$: then $[P\tilde{R},\tilde{S}]=[\tilde{W},\tilde{W}']=[\tilde{R},P\tilde{S}]$, so $P^{\dagger}=P$. The $J$-commuting definite-orthogonal case is the special one, not the general one: the Krein-orthogonal projection onto the positive line $\mathbb{C}(e_0+\tfrac12 e_1)$ is $J$-self-adjoint, is not self-adjoint for $\langle\cdot,\cdot\rangle$, and does not commute with $J$. For the sign, $\pi_{+}=J\cdot\pi_{+}$ with $\pi_{+}\geq0$ for $\langle\cdot,\cdot\rangle$, so $\pi_{+}\in\mathcal{P}_{J}$; while $\pi_{-}=J\cdot(-\pi_{-})$ with $-\pi_{-}\leq0$, so $\pi_{-}\notin\mathcal{P}_{J}$ and $-\pi_{-}\in\mathcal{P}_{J}$. Since $\mathcal{P}_{J}=J\cdot\{S\geq0\}$ and the extreme rays of $\{S\geq0\}$ are the rank-one positive operators $|\tilde{Q}\rangle\langle\tilde{Q}|$, the extreme rays of $\mathcal{P}_{J}$ are their images, which are the rank-one $J$-projections.

## The Cartan Involution and the $J$-Unitary Group

**Theorem (the $J$-adjoint involution).** On the invertible operators the map

$$
\theta_{J}(T)=\bigl(T^{\dagger}\bigr)^{-1}
$$

is an involution whose fixed set is exactly the $J$-unitary group $U_{J}(\mathbb{B})\cong U(1,3)$; its differential at the identity is $-{}^{\dagger}$, and the fixed Lie algebra is the $J$-skew part $\mathfrak{u}(1,3)$.

**Proof.** $\theta_{J}^{2}(T)=\bigl((T^{\dagger})^{-1}\bigr)^{\dagger}{}^{-1}=(T^{\dagger\dagger})^{-1}{}^{-1}=T$, using $(S^{-1})^{\dagger}=(S^{\dagger})^{-1}$ and $T^{\dagger\dagger}=T$; the fixed-set identity $\theta_{J}(T)=T\iff T^{\dagger}T=e_0$ is the definition of $J$-unitarity, and the group is $U(1,3)$ (*The Krein Isometry Group and Its $J$-Contractions*). The differential on $X$ is $-X^{\dagger}$ and the fixed elements are the $J$-skew operators, which are exactly $\mathfrak{u}(1,3)$ (*The Krein Cartan Decomposition of the Operator Algebra*).

**Remark (why this is not a Cartan involution).** Its fixed group $U_{J}(\mathbb{B})\cong U(1,3)$ is **non-compact**, so $\theta_{J}$ cannot be the Cartan involution of the reductive group of operators, whose fixed group is compact by definition. The involution attached to the Krein form is the *Krein-adjoint* involution; the Cartan involution that goes with it is the restriction of the definite involution $\theta_{0}(T)=(T^{*})^{-1}$ to $U(1,3)$, whose fixed group is the maximal compact subgroup $U(1)\times U(3)$, and the resulting symmetric space $U(1,3)/(U(1)\times U(3))$ is the complex hyperbolic space of real dimension $6$ (*The Krein Cartan Decomposition of the Operator Algebra*). This is the reason the indefinite positivity sits beside the definite one and not inside it.

## Worked Examples

**The centre.** $\tilde{Q}=te_0$, $t\in\mathbb{R}$: $[\tilde{Q},\tilde{Q}]=t^{2}\geq0$, so the positive part lies in the cone, and $t\neq0$ in the interior.

**A vector element.** $\tilde{Q}=e_2$: $[\tilde{Q},\tilde{Q}]=-1<0$, outside the cone and in the negative part.

**An isotropic element of the boundary.** $\tilde{Q}=e_0+e_2$: $[\tilde{Q},\tilde{Q}]=0$, on the boundary; note it is **not** in the Hermitian cone, since its matrix is not positive semidefinite, and it is not a zero divisor, since $N=2$.

**A Hermitian element in both cones.** $\tilde{Q}=2e_0+ie_1$: $\tilde{Q}\in\mathbb{M}_{+}$ with $N=4-1=3>0$ and scalar part $2>0$, so $\tilde{Q}\in P$ and hence in $P_{K}$; the polar decomposition of *The Unitary Group of the Biquaternion Algebra* writes it as $\tilde{U}\tilde{P}$ with both factors in their cones.

**A non-convexity witness.** $\tilde Q_1=e_0+e_2$ and $\tilde Q_2=-e_0+e_2$ are both in $P_{K}$, but their midpoint $e_2$ is not.

**A $J$-positive operator that is not Hilbert-positive.** $J={}^{\natural}$ itself: $J\in\mathcal{P}_{J}$ with $[J\tilde{Q},\tilde{Q}]=\|\tilde{Q}\|_E^{2}$, while the Hilbert spectrum of $J$ contains $-1$.

## Summary

The **Krein cone** of the algebra is $P_{K}=\{\tilde{Q}:[\tilde{Q},\tilde{Q}]\geq0\}=\{\|c\|_E\geq\|v\|_E\}$; it is a closed contractible cone, homogeneous but neither convex nor pointed, with interior $\simeq S^{1}$ and boundary the Krein null set of dimension $7$. On the Hermitian subspace it is the full light cone of the interval form, and its future nappe is the **Hermitian cone** $P=\{\tilde{Q}^{\dagger}\tilde{Q}\}$ of the dagger; so $P\subseteq P_{K}$ and the two are different objects. On operators, the **$J$-positive cone** $\mathcal{P}_{J}=\{T=T^{\dagger},\ [T\tilde{Q},\tilde{Q}]\geq0\}=J\cdot\{S\geq0\}$ is the image of the Hilbert positive cone under $J$, hence closed and convex; it contains $J$ itself but not the identity, and its extreme rays are the rank-one $J$-projections. The $J$-projections are the Krein-orthogonal projections onto the non-degenerate subspaces, of which the definite-orthogonal projections commuting with $J$ — in particular $\pi_{\pm}$ — are the special case; among $\pi_{\pm}$, $\pi_{+}$ is $J$-positive and $\pi_{-}$ is $J$-negative. The involution $\theta_{J}(T)=(T^{\dagger})^{-1}$ has fixed set the $J$-unitary group $U_{J}(\mathbb{B})\cong U(1,3)$, which is non-compact: it is not a Cartan involution, and the Cartan involution that goes with it has the compact fixed group $U(1)\times U(3)$ (*The Krein Cartan Decomposition of the Operator Algebra*).

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{K}=\{[\tilde{Q},\tilde{Q}]\geq0\}=\{\lVert c\rVert_E\geq\lVert v\rVert_E\}$ | The Krein cone; closed, contractible, non-convex |
| $P_{K}^{\circ}\simeq S^{1}$ | Interior of the Krein cone |
| $\partial P_{K}=\{[\tilde{Q},\tilde{Q}]=0\}$ | Krein null set; real cone of dimension $7$ |
| $P_{K}\cap\mathbb{M}_{+}$ | Light cone of the interval form on the Hermitian subspace |
| $P=\{\tilde{Q}^{\dagger}\tilde{Q}\}$ | Hermitian cone; the future nappe, $P\subseteq P_{K}$ |
| $\mathcal{P}_{J}=J\cdot\{S\geq0\}$ | The $J$-positive cone; convex, contains $J$ |
| $\pi_{\pm}=\tfrac12(\mathrm{id}\pm J)$ | The $J$-projections; spectral projections of $J$ |
| $\mathcal{P}_{J}=J\cdot\{S\geq0\}$ | The $J$-positive cone; contains $J$, not $\mathrm{id}$ |
| $J\,|\tilde{Q}\rangle\langle\tilde{Q}|$, $\lVert\tilde{Q}\rVert_E=1$ | The extreme rays of $\mathcal{P}_{J}$ |
| $\theta_{J}(T)=(T^{\dagger})^{-1}$ | The $J$-adjoint involution; fixed set $U_{J}(\mathbb{B})\cong U(1,3)$, non-compact |

## Further Reading

- *Krein Algebras* (`articles_maths/krein-algebras.md`) and *Self-Adjoint Elements and the Positive Cone* (`articles_maths/self-adjoint-elements-and-the-positive-cone.md`), for the general indefinite cone and order
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for $J$ and the two orders
- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the form and its null set
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the $J$-positive cone and the $J$-projections
- *The Krein Isometry Group and Its $J$-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for the group $U(1,3)$ and its maximal compact part
- *The Krein Cartan Decomposition of the Operator Algebra* (`articles_maths/the-krein-cartan-decomposition-of-the-operator-algebra.md`), for $\mathfrak{u}(1,3)$, the Jordan part and the symmetric space
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the definite cone and the Cartan involution used here
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), and Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the indefinite cone and the Cartan involution
