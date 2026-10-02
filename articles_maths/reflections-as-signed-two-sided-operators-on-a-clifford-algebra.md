
# __Reflections as Signed Two-Sided Operators on a Clifford Algebra__

## Introduction

A reflection of a quadratic space is a motion with a hyperplane of fixed points, and on a Clifford algebra it is realised by a two-sided operator: for a vector $u$ with $q(u)\ne0$ the signed sandwich by $(u,u^{-1})$ is exactly the reflection $\rho_u$ in the hyperplane $u^{\perp}$. This raises the question of a correspondence — which signed two-sided operators act on the quadratic space by an involution, and are they exactly the reflections? — and the answer separates the non-degenerate case, where the correspondence is exact and Cartan–Dieudonné explains it, from the degenerate case, where it fails: isotropic vectors generate no reflection, the transvections of the radical are isometries that no sandwich sees, and the reflection length no longer describes the orthogonal group.

The article reads the reflections as the involutive members of the signed family. The reflection formula and the geometry of a single reflection are *The Signed Sandwich on a Clifford Algebra*; here the emphasis is the correspondence and its failure, which is the reason the non-degeneracy hypothesis of the corpus cannot be dropped silently. The correspondence is a bijection between the nonsingular vectors up to scalar and the reflections, and the elements of the orthogonal group acting by an involution with a fixed hyperplane of codimension one are exactly the reflections; the degenerate case breaks the bijection in two ways, by isotropic vectors that are not invertible and by the radical directions that the conjugation cannot move.

**The boundaries.** The reflections, the versor action and Cartan–Dieudonné are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the signed sandwich, its composition and the reflection formula are *The Signed Sandwich on a Clifford Algebra* and *Two-Sided Operators with the Signed Product*. The radical, the reduced form and the structure of a degenerate Clifford algebra are *Degenerate Clifford Algebras and the Radical*; the transvections of a quadratic space are *The Orthogonal Group of a Quadratic Space*. The base is a field $F$ of characteristic not $2$, $q$ a quadratic form on a finite-dimensional space $V$ with polar form $B$ and $q(u)=B(u,u)$; the form is non-degenerate unless the contrary is said.

## The Correspondence

### Reflections and Involutions

**Definition.** A **reflection** of $(V,q)$ is the orthogonal transformation $\rho_u(v)=v-2B(v,u)q(u)^{-1}u$ attached to a vector $u$ with $q(u)\ne0$; it fixes the hyperplane $u^{\perp}$ pointwise and negates $u$.

**Proposition (the correspondence for a non-degenerate form).** Let $q$ be non-degenerate. The map

$$
\{u\in V : q(u)\ne0\}\big/\sim \ \longrightarrow\ \{\text{reflections of }(V,q)\}, \qquad [u]\mapsto\rho_u ,
$$

where $u\sim\lambda u$ for $\lambda\in F^{\times}$, is a bijection. Every reflection is a signed two-sided operator, $T^{\alpha}_{u,u^{-1}}=\rho_u$, and conversely every signed sandwich by a unit acting on $V$ by an involution with a fixed hyperplane of codimension one is a reflection.

**Proof.** The map is well defined because $\rho_{\lambda u}=\rho_u$, and injective because $\rho_u=\rho_{u'}$ forces both to be the same involution, hence the fixed hyperplanes and the negated lines to coincide, so $u'$ is a scalar multiple of $u$; it is surjective because every reflection has the form $\rho_u$ for a vector $u$ normal to its fixed hyperplane, and $u$ is nonsingular since the hyperplane is non-isotropic in a non-degenerate space. The realisation by the sandwich is the reflection formula of *The Signed Sandwich on a Clifford Algebra*. For the converse, a signed sandwich by a unit that acts on $V$ as an involution with a codimension-one fixed space is an orthogonal involution whose $(-1)$-eigenspace on $V$ is a line $\langle u\rangle$; such a transformation is $v\mapsto v-2\frac{B(v,u)}{q(u)}u$ for a generator $u$ of the line, and it is therefore a reflection.

**Remark (the two-to-one and the scalar ambiguity).** The correspondence is two-to-one between vectors and reflections — $u$ and $-u$ give the same reflection — and passes to the quotient by scalars. The signed sandwiches $T^{\alpha}_{u,u^{-1}}$ and $T^{\alpha}_{\lambda u,(\lambda u)^{-1}}$ therefore coincide, and the indeterminacy of the correspondence is the same central-scalar indeterminacy as in the parametrisation of the two-sided family.

**Proposition (involutions with a fixed hyperplane).** Let $\tau$ be an orthogonal transformation of a non-degenerate $(V,q)$. Then $\tau$ is a reflection if and only if $\tau^2=\operatorname{id}$, $\tau\ne\operatorname{id}$ and the fixed space of $\tau$ has codimension one. Equivalently, the reflections are exactly the nontrivial orthogonal involutions with a codimension-one fixed space.

**Proof.** A reflection is an involution with a codimension-one fixed space, as in *The Signed Sandwich on a Clifford Algebra*. Conversely an orthogonal involution is diagonalisable with eigenvalues $\pm1$, and the fixed space is the $(+1)$-eigenspace; if its codimension is one, the $(-1)$-eigenspace is a line $\langle u\rangle$ orthogonal to the fixed space, and the transformation is $v\mapsto v-2\frac{B(v,u)}{q(u)}u$, the reflection.

### The Case of an Isotropic Vector

**Proposition (the failure for an isotropic vector).** Let $u\in V$ with $q(u)=0$ and $u\ne0$. Then $u$ is not invertible in $\mathrm{Cl}(V,q)$ and the expression $\rho_u(v)=v-2B(v,u)q(u)^{-1}u$ is not defined; there is no signed sandwich $T^{\alpha}_{u,u^{-1}}$, and the reflection in the hyperplane orthogonal to $u$ does not exist as a motion: a hyperplane containing an isotropic vector is not the fixed space of a reflection of the non-degenerate form.

**Proof.** The vector$u$ has $u^2=q(u)=0$, so $u$ is a zero divisor and not a unit, and $T^{\alpha}_{u,u^{-1}}$ is not defined. The hyperplane $u^{\perp}$ is degenerate, and an orthogonal involution fixing it has its $(-1)$-eigenspace a line $\langle w\rangle$ with $B(u,w)=0$ and $w$ nonsingular, in which case the reflection is $\rho_w$, not $\rho_u$; the correspondence attaches a reflection to a nonsingular normal vector and there is none normal to a hyperplane containing an isotropic vector in the intended way. In an indefinite form the isotropic vectors are exactly the obstructions to the naive formula, and the motions they produce are the transvections, treated below.

## The Degenerate Case

### The Radical and the Invisible Directions

**Given.** The **radical** of $q$ is $\operatorname{rad}(q)=\{r\in V : B(r,w)=0\ \text{for all }w\}$; it is totally isotropic, and for a degenerate form it is nonzero. The reduced form $\bar q$ on a complement $W$ of the radical is non-degenerate, and the Clifford algebra is $\mathrm{Cl}(V,q)=\mathrm{Cl}(W,\bar q)\,\hat\otimes\,\Lambda(\operatorname{rad}(q))$ by *Degenerate Clifford Algebras and the Radical*, with $r^2=0$ for $r$ in the radical.

**Proposition (the failure of the reflection correspondence).** Let $q$ be degenerate with radical $R\ne0$, and write $V=W\oplus R$ with $\bar q=q|_W$ non-degenerate. Then:

**(a)** the reflections $\rho_u$ exist for the nonsingular vectors $u\in W$, and they generate the subgroup of $O(V,q)$ acting trivially on $R$;

**(b)** an isometry $t$ of $V$ with $t(r)=r+\phi(r)u_0$ for $r\in R$ and a vector $u_0\in W$, where $\phi$ is a linear functional vanishing on $W^{\perp}\cap R$, is an orthogonal transformation fixing $W^{\perp}\cap R$ pointwise and acting as the identity on $V/R$; these **transvections** by the radical are isometries;

**(c)** the transvections of $R$ are **not** realised by any signed two-sided operator, because a sandwich by an invertible element of the Clifford algebra acts on $V$ through $\mathrm{Cl}(W,\bar q)$ and fixes $R$ pointwise.

**Proof.** (a) is the non-degenerate correspondence for $\bar q$, transported to $W$; the reflection $\rho_u$ for $u\in W$ fixes $R$ since $B(u,R)=0$, so it acts trivially on $R$. (b) For $v=w+r$ with $r\in R$, $q(v)=q(w)$ and $B$ vanishes on $R$; the transformation $t(v)=v+\phi(r)u_0$ satisfies $q(tv)=q(w)=q(v)$ and preserves $B$ because the cross terms involve $B(u_0,R)=0$, so it is an isometry; it fixes $R$ modulo $u_0$ and is the identity on $V/R$. (c) An element $a$ of the Clifford algebra preserves $V$ under $x\mapsto a\alpha(x)a^{-1}$ only if its image in the radical factor is central; the radical generators $r$ satisfy $r^2=0$ and the conjugation by any unit acts on $R$ trivially in the reduction to $\mathrm{Cl}(W,\bar q)$, so the displacement $r\mapsto r+\phi(r)u_0$ is not produced. The classification of the versors of a degenerate Clifford algebra is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and *Degenerate Clifford Algebras and the Radical*, where the reduction is made.

**Remark (why the failure matters).** In the non-degenerate case the signed sandwiches and the reflections generate the orthogonal group by Cartan–Dieudonné, so the whole geometry of the motions is carried by the algebra. In the degenerate case they generate only the subgroup acting trivially on the radical, and the transvections are outside it; the reflection length therefore measures the non-degenerate part and says nothing about the radical directions. The hypothesis of non-degeneracy in *The Signed Sandwich on a Clifford Algebra* is thus not a convenience but a genuine restriction.

### The Degenerate Line

**Example.** Let $V=\langle r\rangle$ with $q(r)=0$, the smallest degenerate form. Then $q$ is the zero form, every nonzero linear map is an isometry, so $O(V,q)=F^{\times}$; the Clifford algebra is $\mathrm{Cl}=\mathrm{Cl}_0\oplus\mathrm{Cl}_1$ with $r^2=0$, the ring of dual numbers $F[\varepsilon]/(\varepsilon^2)$, and the only signed two-sided operators are the scalars $T^{\alpha}_{\lambda,\mu}(x)=\lambda\mu\,\alpha(x)$. Their action on $V$ is trivial, so the image of the signed family in $O(V,q)$ is $\{1\}$ while $O(V,q)=F^{\times}$: the correspondence collapses completely.

## Worked Cases

### A Non-Degenerate Reflection

For $V$ of dimension two with the split form $e_1^2=1$, $e_2^2=-1$ and $u=e_1+e_2$, the vector has $q(u)=0$ and generates no reflection, as in the proposition; for $u=e_1$, $q(u)=1$ and $T^{\alpha}_{e_1,e_1}(v)=e_1\alpha(v)e_1$ sends $e_1\mapsto-e_1$, $e_2\mapsto e_2$, the reflection in $\langle e_2\rangle$. The pair $(e_1,-e_1)$ and $(e_1,e_1)$ gives the two signed sandwiches with the same action, exhibiting the two-to-one ambiguity.

### The Transvection of the Hyperbolic Line

Let $V=\langle e,r\rangle$ with $q(e)=1$, $q(r)=0$ and $B(e,r)=0$, so that the form is degenerate with radical $\langle r\rangle$. The transformation $t(e)=e+r$, $t(r)=r$ is an isometry of $q$, since $q(e+r)=1$; it is not the identity and not a reflection, and it fixes the radical pointwise and is the identity on $V/\langle r\rangle$. The element $1+r$ is invertible with inverse $1-r$, but its conjugation does not preserve $V$ — it sends $e$ to $e-2er$, outside $V$ — so $1+r$ is not in the Clifford group and the transvection is not realised. This is the smallest witness that the degenerate isometries exceed the signed sandwiches.

### An Isotropic Vector in the Lorentz Plane

For $V$ of dimension two with $q$ of signature $(1,1)$ and $u$ isotropic, the reflection in the isotropic line does not exist as an isometry of the form, and the two isotropic lines are permuted by the hyperbolic rotations rather than fixed by reflections; the correspondence attaches reflections only to the nonsingular vectors, of which the two lines of the standard basis are representatives in the indefinite case.

## Summary

For a **non-degenerate** form, the reflections of the quadratic space are exactly the signed two-sided operators acting by an involution with a codimension-one fixed space: the map $[u]\mapsto\rho_u=T^{\alpha}_{u,u^{-1}}$ is a bijection from the nonsingular vectors modulo scalars to the reflections, with the two-to-one ambiguity $u\sim-u$. The correspondence fails in the **degenerate case**, and in two ways: an isotropic vector $u$ with $q(u)=0$ is not invertible, so no reflection is attached to it; and the **transvections** by the radical, $v\mapsto v+\phi(r)u_0$, are isometries fixing the radical and acting as the identity on $V/\operatorname{rad}(q)$ that no signed sandwich realises, because a sandwich by an invertible element acts on $V$ through the non-degenerate factor of the Clifford algebra. The signed sandwiches therefore generate only the subgroup of $O(V,q)$ acting trivially on the radical, and the Cartan–Dieudonné description of the orthogonal group by reflections is a non-degeneracy statement. The reflection formula and the geometry of a single reflection are *The Signed Sandwich on a Clifford Algebra*; the versors and Cartan–Dieudonné are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the radical and the reduction are *Degenerate Clifford Algebras and the Radical*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_u(v)=v-2B(v,u)q(u)^{-1}u$ | Reflection attached to a nonsingular vector $u$ |
| $T^{\alpha}_{u,u^{-1}}=\rho_u$ | Realisation by the signed sandwich |
| $[u]\mapsto\rho_u$ | Bijection nonsingular vectors $/$ scalars $\to$ reflections, $q$ non-degenerate |
| $q(u)=0$ | Isotropic vector; no reflection, $u$ not a unit |
| $\operatorname{rad}(q)=\{r : B(r,\cdot)=0\}$ | Radical; nonzero for a degenerate form |
| $t(v)=v+\phi(r)u_0$ | Transvection by the radical; an isometry not realised |
| $O(V,q)$, $F^{\times}$ | Orthogonal group; degenerate line case $O=F^{\times}$ |
| $\mathrm{Cl}(W,\bar q)\hat\otimes\Lambda(\operatorname{rad}(q))$ | Structure of the degenerate Clifford algebra |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the reflection correspondence and the versor theory in the non-degenerate case.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 3rd ed. 1971), for the transvections, the orthogonal group of a quadratic space and the failure of Cartan–Dieudonné in the degenerate case.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflection formula and the two conjugation actions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the involutions of the orthogonal group and the reflection length.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Clifford algebra of a degenerate form and the orthogonal group.
