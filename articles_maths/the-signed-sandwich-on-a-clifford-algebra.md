
# __The Signed Sandwich on a Clifford Algebra__

## Introduction

The two-sided sandwich of a Clifford algebra sends $x$ to $a\,x\,b$, and it acts on the quadratic space $V$ by orthogonal transformations up to a sign: for a vector $u$ the ordinary sandwich by $(u,u^{-1})$ is the **negative** of the reflection in $u^{\perp}$. Inserting the grade involution into the middle of the product repairs the sign. The **signed sandwich** is the operator

$$
T^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b ,
$$

where $\alpha$ is the grade involution of the algebra; it is the ordinary sandwich of the twisted element, $T^{\alpha}_{a,b}=T_{a,b}\circ\alpha$, and for a vector $u$ with $q(u)\ne0$ it is exactly the reflection $\rho_u$ on $V$. This is the geometric reason the signed family exists: the reflections of the quadratic space are the elementary motions, and the signed sandwich carries them.

The article treats the signed sandwich from the side of the geometry of the chosen form. The operator itself, its composition law and its coset structure belong to *Two-Sided Operators with the Signed Product*, and the one-sided factors to *One-Sided Operators with the Signed Product*; both are Part II's and are quoted. What is added here is the reading on $V$: the reflection formula, the hyperplane fixed by the reflection, the parities of the determinant, the generation of the orthogonal group by the reflections, the versor action and the relation to the two-sided operators of the category. A word of disambiguation is needed at the start, because the corpus uses "signed" in two senses: the **signed inner conjugation** $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)yx^{-1}$ of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* twists the **parameter**, while the signed sandwich twists the **argument**; only the second is the subject of this article.

**The boundaries.** The ordinary sandwich, its composition and its indeterminacy are *The Sandwich on a Clifford Algebra*; the signed two-sided operator, its composition law and its coset structure are *Two-Sided Operators with the Signed Product*; the signed left and right factors are *One-Sided Operators with the Signed Product*. The reflections, the Clifford group, the versors and Cartan–Dieudonné are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, and the failure of the reflection correspondence for a degenerate form is *Reflections as Signed Two-Sided Operators on a Clifford Algebra*, written next in this group. The base is a field $F$ of characteristic not $2$, $q$ a non-degenerate quadratic form on a finite-dimensional space $V$ with polar form $B$, and $q(u)=B(u,u)$, $uv+vu=2B(u,v)$, so that $u^2=q(u)$.

## The Operator and Its Sign

### Definition and Relation to the Unsigned Sandwich

**Definition.** For $a,b\in\mathrm{Cl}(V,q)$ the **signed sandwich** is the $F$-linear operator

$$
T^{\alpha}_{a,b} : \mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q), \qquad T^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b .
$$

**Proposition (the relation to the unsigned family).** $T^{\alpha}_{a,b}=T_{a,b}\circ\alpha=\alpha\circ T_{\alpha(a),\alpha(b)}$, and $T^{\alpha}_{1,1}=\alpha$. The signed sandwich is the ordinary sandwich composed with the grade involution, and the map $T_{a,b}\mapsto T_{a,b}\alpha$ is a bijection from the ordinary two-sided operators onto the signed ones.

**Proof.** Immediate from $\alpha(xb)=\alpha(x)\alpha(b)$ and the definition; the bijection has inverse $S\mapsto S\circ\alpha$. The statement and its consequences are *Two-Sided Operators with the Signed Product*, quoted.

**Proposition (the composition law and the coset structure).** For all $a,b,c,d$,

$$
T^{\alpha}_{a,b}T^{\alpha}_{c,d}=T_{a\alpha(c),\,\alpha(d)b},
\qquad
T^{\alpha}_{a,b}T_{c,d}=T^{\alpha}_{a\alpha(c),\,\alpha(d)b},
\qquad
T_{a,b}T^{\alpha}_{c,d}=T^{\alpha}_{ac,\,db} .
$$

The composite of two signed sandwiches is an **ordinary** sandwich, the two grade involutions cancelling; the family of invertible signed sandwiches is the coset $\mathcal{T}\alpha$ of the group $\mathcal{T}$ of ordinary ones, contains no identity, and is a torsor and not a group.

**Proof.** The computation is in *Two-Sided Operators with the Signed Product*: $T^{\alpha}_{a,b}T^{\alpha}_{c,d}(x)=a\alpha(c)x\alpha(d)b$, and the middle factor $\alpha^2(x)=x$ is untwisted; the parity of the number of factors decides whether the composite is signed, and the two-factor composite $T^{\alpha}_{a,b}T^{\alpha}_{\alpha(a^{-1}),\alpha(b^{-1})}=\operatorname{id}$ shows that the identity lies in the group generated but not in the coset.

### The Two Senses of "Signed"

**Remark (parameter against argument).** The corpus has two families that carry the adjective signed. The **signed inner conjugation** is $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)yx^{-1}$, where the grade involution is applied to the **parameter** $x$; the operator is $\varepsilon_x$ times the inner conjugation, and its geometry is the geometry of the versors. The **signed sandwich** applies the involution to the **argument** $x$; it is $T_{a,b}\circ\alpha$, and its geometry is the geometry of the reflections. The two coincide neither in definition nor in purpose, and the article treats only the second; the first is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, and the distinction is the reason both names exist.

**Remark (the parity of the sign).** The two families satisfy different composition laws because an automorphism acts on the argument by pulling through a product, while it acts on the parameter by pushing forward; this is the asymmetry recorded in *One-Sided Operators with the Signed Product*, and it is the reason the arguments of the signed sandwich are the plain elements while the arguments of the signed inner conjugation are the versors.

## The Reflections

### The Reflection Formula

**Theorem (the reflections).** Let $u\in V$ with $q(u)\ne0$. Then the signed sandwich by $(u,u^{-1})$ acts on the quadratic space as the reflection in the hyperplane $u^{\perp}$,

$$
T^{\alpha}_{u,u^{-1}}(v) = u\,\alpha(v)\,u^{-1} = -u\,v\,u^{-1} = \rho_u(v) = v - 2\,\frac{B(v,u)}{q(u)}\,u , \qquad v\in V .
$$

**Proof.** A vector is odd, so $\alpha(v)=-v$ and $T^{\alpha}_{u,u^{-1}}(v)=-uvu^{-1}$. Since $uv+vu=2B(u,v)$ and $u^2=q(u)$, the product $uvu=2B(u,v)u-q(u)v$, and $u^{-1}=u\,q(u)^{-1}$; substituting gives $-uvu^{-1}=(q(u)v-2B(u,v)u)q(u)^{-1}=\rho_u(v)$. The formula is the reflection of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, quoted in the form needed here.

**Corollary (the ordinary sandwich gives the negative).** The ordinary sandwich by $(u,u^{-1})$ is the negative of the reflection, $T_{u,u^{-1}}(v)=uvu^{-1}=-\rho_u(v)$. The signed product inserts exactly the sign that repairs this, at the cost of the identity: the signed family has no identity because $\alpha$ is not the identity on the odd part. This is the trade recorded in *Two-Sided Operators with the Signed Product*.

### The Geometry of a Reflection

**Proposition.** For $u\in V$ with $q(u)\ne0$ the reflection $\rho_u$ fixes pointwise the hyperplane $u^{\perp}$ and sends $u$ to $-u$; it is an involution, $\rho_u^2=\operatorname{id}$, it preserves the form, $\rho_u\in O(V,q)$, and its determinant is $-1$.

**Proof.** The fixed locus is immediate from the formula: $B(v,u)=0$ gives $\rho_u(v)=v$, and $\rho_u(u)=u-2q(u)q(u)^{-1}u=-u$. The square is the identity because a reflection of order two has $\rho_u(-u)=u$; the form is preserved because $\rho_u$ acts on the orthogonal decomposition $\langle u\rangle\oplus u^{\perp}$ as $-1$ on the line and $+1$ on the hyperplane; the determinant is the product $(-1)\cdot(+1)^{n-1}=-1$.

**Remark (reflection and hyperplane are reciprocal).** The hyperplane $u^{\perp}$ does not determine the vector $u$, only its line; two proportional vectors $u$ and $\lambda u$ with $\lambda\ne0$ give the same reflection when $q(\lambda u)\ne0$, since $\rho_{\lambda u}=\rho_u$. The correspondence between reflections and vectors is therefore two-to-one up to scalars, and the signed sandwiches $T^{\alpha}_{u,u^{-1}}$ and $T^{\alpha}_{\lambda u,(\lambda u)^{-1}}$ coincide; this is the same indeterminacy as the central-unit kernel of the parametrisation of the two-sided family.

**Proposition (the determinant parity).** A composition of $k$ reflections is an element of $O(V,q)$ with determinant $(-1)^k$: it is a rotation when $k$ is even and a reflection-times-rotation when $k$ is odd. The signed sandwich by the parameter pair corresponding to a product of vectors $u_1\cdots u_k$ acts on $V$ as the product of the reflections $\rho_{u_1}\cdots\rho_{u_k}$.

**Proof.** The determinant of a product is the product of the determinants, each $-1$; the action of a composition of the signed sandwiches is the composition of the actions, and the sandwich by a product of vectors is the product of the sandwiches under the composition law, the parity deciding whether the composite is signed.

## The Actions on the Quadratic Space

**Theorem (Cartan–Dieudonné, quoted).** Every element of the orthogonal group $O(V,q)$ is a product of reflections, and the number of factors is the reflection length of the element, with parity the determinant. Consequently the reflections, and hence the signed sandwiches, generate the orthogonal group of the quadratic space.

**Proof sketch.** The classical theorem of Cartan and Dieudonné: an isometry is written as a product of reflections in the hyperplanes it moves, and the length count is the dimension of the moved subspace; the proof is in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

**Theorem (the versor action, quoted).** The invertible elements of the Clifford algebra that preserve $V$ under the signed conjugation form the **Clifford group** $\Gamma$, the products of units of $V$ act on $V$ through the signed sandwich as orthogonal transformations, and the resulting map $\Gamma\to O(V,q)$ is surjective with kernel the central units. Its restriction to the products of an even number of units is the spin group, and the odd coset carries the reflections.

**Proof sketch.** An element $a$ preserves $V$ under $x\mapsto a\alpha(x)a^{-1}$ exactly when it is a versor, which is the definition of the Clifford group; the map to $O(V,q)$ is a group homomorphism by the composition law, it is surjective by Cartan–Dieudonné, and its kernel is computed from the condition that the conjugated vector equal the vector for all vectors, which forces the element central. This is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, quoted.

**Remark (why the signed family is the geometric one).** The unsigned sandwich by a vector realises $-\rho_u$, so a product of $k$ unsigned sandwiches realises $(-1)^k$ times the corresponding orthogonal transformation: on the even part it is correct, on the odd part it carries a sign. The signed sandwich is the family that acts on $V$ by the orthogonal transformation itself, and it is therefore the family used for the geometry of the orthogonal group, while the unsigned one is used for the algebra of the two-sided operators. The distinction is the whole content of the adjective.

## Worked Cases

### A Reflection in the Negative-Definite Plane

For $V$ of dimension two with $e_1^2=e_2^2=-1$, let $u=e_1$, so $q(u)=-1$, $u^{-1}=-e_1$ and $\alpha(v)=-v$ for every vector. Then $T^{\alpha}_{e_1,-e_1}(v)=e_1\alpha(v)(-e_1)=e_1ve_1$, and on the basis $T^{\alpha}_{e_1,-e_1}(e_1)=-e_1$, $T^{\alpha}_{e_1,-e_1}(e_2)=e_2$: the reflection in the line $e_1^{\perp}=\langle e_2\rangle$; the ordinary sandwich would have given $(-e_1,-e_2)=-\rho_{e_1}$.

### A Hyperbolic Reflection

For $V$ of dimension two with the split form $e_1^2=1$, $e_2^2=-1$, take $u=e_1+e_2$, so $q(u)=0$: the vector is isotropic and the reflection formula does not apply. Take instead $u=e_1$, $q(u)=1$, $u^{-1}=u$; then $T^{\alpha}_{e_1,e_1}(v)=e_1\alpha(v)e_1$, which fixes $e_2$ and sends $e_1$ to $-e_1$, the reflection in the line $\langle e_2\rangle$. The isotropic vector $e_1+e_2$ generates no reflection, and this is the first sign that the correspondence between vectors and reflections fails for a degenerate or isotropic datum, the subject of *Reflections as Signed Two-Sided Operators on a Clifford Algebra*.

### A Rotation of the Lorentz Plane

For $x=e_1e_2$ the element is even and a unit with $x^{-1}=e_2e_1=-e_1e_2$; the signed sandwich $T^{\alpha}_{x,x^{-1}}(v)=xvx^{-1}$ is the ordinary inner conjugation, since $\alpha$ is the identity on the even part, and its action is the half-turn of the plane $\mathrm{span}(e_1,e_2)$: it sends $e_1\mapsto-e_1$, $e_2\mapsto-e_2$ in the Euclidean case, the rotation of angle $\pi$. The signed and the unsigned sandwiches coincide on the even part of the algebra, and differ only on the odd part, which is where the reflections live.

## Summary

The **signed sandwich** $T^{\alpha}_{a,b}(x)=a\alpha(x)b$ is the ordinary sandwich of the twisted argument, $T^{\alpha}_{a,b}=T_{a,b}\circ\alpha$, and it satisfies $T^{\alpha}_{a,b}T^{\alpha}_{c,d}=T_{a\alpha(c),\alpha(d)b}$: two signed sandwiches compose to an ordinary one, the two grade involutions cancelling, so the invertible signed sandwiches form the **coset** $\mathcal{T}\alpha$, a torsor without identity. The corpus uses "signed" in two senses, and the article separates them: the signed **inner conjugation** twists the parameter and belongs to the versor theory, while the signed **sandwich** twists the argument and belongs to the reflection theory. The geometric content is the **reflection formula** $T^{\alpha}_{u,u^{-1}}(v)=u\alpha(v)u^{-1}=-uvu^{-1}=\rho_u(v)$ for a vector $u$ with $q(u)\ne0$, where the ordinary sandwich gave the negative $-\rho_u$; the reflection fixes pointwise the hyperplane $u^{\perp}$ and negates $u$, it is an orthogonal involution of determinant $-1$, and the composition of $k$ of them has determinant $(-1)^k$. By Cartan–Dieudonné the reflections generate the whole orthogonal group $O(V,q)$, and the versor action of the Clifford group realises them through the signed sandwich, with kernel the central units. The operator and its composition law are *Two-Sided Operators with the Signed Product*, the factors are *One-Sided Operators with the Signed Product*, and the degenerate case is *Reflections as Signed Two-Sided Operators on a Clifford Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | Grade involution, $\alpha(x)=(-1)^{\deg x}x$ on homogeneous $x$ |
| $T^{\alpha}_{a,b}(x)=a\alpha(x)b$ | Signed sandwich |
| $T^{\alpha}_{a,b}=T_{a,b}\circ\alpha$ | Relation to the ordinary sandwich |
| $\mathcal{T}\alpha$ | The signed coset of the ordinary two-sided group; a torsor |
| $\rho_u(v)=v-2B(v,u)q(u)^{-1}u$ | Reflection in $u^{\perp}$ |
| $T^{\alpha}_{u,u^{-1}}=\rho_u$, $T_{u,u^{-1}}=-\rho_u$ | The sign repaired by the signed product |
| $q(u)=B(u,u)$, $uv+vu=2B(u,v)$ | Form and Clifford relation |
| $O(V,q)$, $\Gamma$ | Orthogonal group and Clifford (versor) group |
| Cartan–Dieudonné | Every isometry is a product of reflections |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the reflections, the versor action and the signed conjugation.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the two conjugation actions on the vectors and the reflection formula.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution and the two-sided operators.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the reflection formula in the low-dimensional algebras and the sign conventions.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 3rd ed. 1971), for Cartan–Dieudonné and the generation of the orthogonal group by reflections.
