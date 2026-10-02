
# __The Involution on a Complex Vector Space__

## Introduction

A complex vector space carries two natural involutions, and the whole of its real structure is their interplay. The first is the **complex structure**: an $\mathbb{R}$-linear operator
$$
J : V \longrightarrow V, \qquad J^2 = -\mathrm{id},
$$
whose square is $-1$ and which encodes the multiplication by $i$ of $V$ as a real vector space. The second is the **conjugation**, the real structure: an $\mathbb{R}$-linear map
$$
c : V \longrightarrow V, \qquad c^2 = \mathrm{id}, \qquad c(iv) = -i\,c(v),
$$
that is a real-linear involution which is **conjugate-linear**; its fixed set $V_0 = \{v : c(v) = v\}$ is a **real form** of $V$, of real dimension equal to the complex dimension, with $V = V_0\oplus JV_0$. The conjugation is the linear form of complex conjugation, of the real structure of a complex manifold, and of the descent: the conjugate-linear involution is the datum that makes $V$ the complexification of the real space $V_0$, and the complex structure together with the conjugation generate the relations
$$
J^2 = -\mathrm{id}, \qquad c^2 = \mathrm{id}, \qquad Jc = -cJ,
$$
which are the relations of the real Clifford algebra $\mathrm{Cl}_{1,1}\cong M_2(\mathbb R)$. This linear article is the model of *Real Structures on a Complex Manifold* and *Complex Manifolds with an Antiholomorphic Involution*; the product $K = Jc$ is a second real structure, generically distinct from $c$, and the pair of real structures it produces is the linear image of the two real forms of a complex manifold.

The article has three sections: the real structure and the complex structure, and their anticommutation; the conjugation and the Hermitian form; and the transport of the real structure to the endomorphism algebra. The complex structure operator, the almost complex structure and the type decomposition are *The Almost Complex Operator*, *Hermitian Geometry and Almost Complex Structures* and *Operators on a Complex Manifold*; the Hermitian forms, the unitary group and the signatures are *Hermitian Geometry and the Unitary Group*, later in this category; the real structures on the manifold and on the operator layer are *Real Structures on a Complex Manifold* and *Real Structures on the Operator Layer*; the real forms and the descent are *Real Structures on Varieties and Galois Descent*; the Clifford algebra is *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*. None of that is re-derived.

Throughout, $V$ is a complex vector space of dimension $m$, regarded as a real vector space of dimension $2m$ with the complex structure $J$, $c$ is a conjugation, $V_0 = \operatorname{Fix}(c)$ the real form, $h$ is a positive-definite Hermitian form on $V$, and $\operatorname{End}_{\mathbb C}(V)$ is the endomorphism algebra.

## The Real Structure and the Complex Structure

**Definition.** A **conjugation** (or **real structure**) on the complex vector space $V$ is a conjugate-linear involution $c$: an $\mathbb{R}$-linear map with $c^2 = \mathrm{id}$ and $c(iv) = -ic(v)$; its fixed set $V_0 = \operatorname{Fix}(c)$ is the **real form** of $c$. A **real basis** of $V$ is a real basis of a real form.

**Proposition (the relations).** The complex structure and any conjugation anticommute,
$$
Jc = -cJ,
$$
and with $J^2 = -\mathrm{id}$, $c^2 = \mathrm{id}$, $cJ=-Jc$ they generate the Clifford algebra $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$; the product $K = Jc$ is a real structure with $K^2 = \mathrm{id}$ and $KJ = -JK$, distinct from $c$ unless $V_0$ is $J$-stable.

**Proof.** $c(iv) = -ic(v)$ is exactly $cJ = -Jc$. For $K = Jc$ one has $K^2 = JcJc = J(-Jc)c = -J^2c^2 = \mathrm{id}$, using $J^2 = -\mathrm{id}$ and $c^2 = \mathrm{id}$; and $KJ = JcJ = J(-Jc) = -J^2c = c$, while $JK = J(Jc) = -c$, so $K$ anticommutes with $J$. The relations $c^2 = 1$, $J^2 = -1$, $cJ = -Jc$ are exactly the relations $e_1^2 = 1$, $e_2^2 = -1$, $e_1e_2 = -e_2e_1$ of $\mathrm{Cl}_{1,1}\cong M_2(\mathbb R)$ with $e_1 = c$ and $e_2 = J$, so $V$ is a module over $\mathrm{Cl}_{1,1}$. This is *Clifford Algebras*.

**Proposition (the real form and the tangent decomposition).** The real form $V_0$ has real dimension $m$, is **totally real**, $V_0\cap JV_0 = 0$, and
$$
V = V_0\oplus JV_0
$$
as real vector spaces; the proof of the corresponding statement for a complex manifold is the split of *Real Structures on a Complex Manifold*.

**Proof.** If $v \in V_0$ then $c(iv) = -i v \neq iv$ for $v\neq0$, so $cv = v$ and a real form contains no $J$-line; hence $V_0\cap JV_0 = 0$. For the sum, a real basis $v_1,\dots,v_m$ of $V_0$ has $iv_1=Jv_1,\dots,iv_m=Jv_m$ independent of $v_1,\dots,v_m$ (else a nontrivial real combination of the $v_k$ is annihilated by $J$), so the $2m$ vectors $v_1,\dots,v_m,Jv_1,\dots,Jv_m$ span $V_\R$; hence $V = V_0\oplus JV_0$.

**Remark (the two real structures).** The conjugation $c$ and its companion $K = Jc$ are two real structures on the same complex space; their real forms $V_0 = \operatorname{Fix}(c)$ and $K_0 = \operatorname{Fix}(K)$ are generic real forms, and they coincide exactly when $V_0$ is $J$-stable, that is when the real structure is the "standard" one for the decomposition $V = V_0\oplus iV_0$. The linear statement that all real structures on $V$ are conjugate by $GL(V)$ is *Complex Manifolds with an Antiholomorphic Involution*; here the structure is the pair $(J, c)$.

## The Conjugation and the Hermitian Form

**Definition.** Let $h$ be a Hermitian form on $V$, conjugate-symmetric and linear in the first argument; a conjugation $c$ is **compatible** with $h$ when
$$
h(cx, cy) = \overline{h(x, y)} \qquad (x, y \in V).
$$

**Proposition (the real and imaginary parts).** If $c$ is compatible with $h$, then on the real form $V_0$ the Hermitian form $h$ is real: $h(x,y) \in \mathbb{R}$ for $x, y \in V_0$, and the real part $g = \operatorname{Re}h$ is a positive-definite symmetric bilinear form on $V_0$ while the imaginary part $\omega = -\operatorname{Im}h$ is an alternating form with $\omega(x, Jy) = g(x,y)$; the sesquilinear decomposition $h = g - i\omega$ holds, with $g$ symmetric and $J$-invariant and $\omega$ antisymmetric and $J$-invariant.

**Proof.** For $x,y \in V_0$ one has $h(x,y) = h(cx,cy) = \overline{h(x,y)}$, so $h(x,y)$ is real; symmetry of the restriction is the conjugate-symmetry of $h$ at real values. The form $g(x,y) = \operatorname{Re}h(x,y)$ is then symmetric and positive definite on $V_0$ and extends to all of $V$ as the real inner product of the underlying real space; the alternating form is $\omega(x,y) = -\operatorname{Im}h(x,y)$, and $\omega(x,Jy) = -\operatorname{Im}h(x,Jy) = \operatorname{Re}h(x,y) = g(x,y)$ by the $\mathbb C$-linearity of $h$ in the second argument... in the first, with the sign fixed by $h = g - i\omega$. The Hermitian form and its positivity are *Hermitian Geometry and the Unitary Group*.

**Corollary (signature of the restriction).** The signature $(p,q)$ of $h$ restricted to a real form is an invariant of the pair $(h, c)$ under the unitary group; it is the classification of the compatible conjugations of *Complex Manifolds with an Antiholomorphic Involution*, and the standard conjugation $z\mapsto\bar z$ on $\mathbb C^m$ gives the definite real form of signature $(m,0)$.

**Proof.** The restriction of $h$ to $V_0$ is a real symmetric form, its signature is invariant under the unitary group by Sylvester's law, and the normal form is the standard one. This is *Hermitian Geometry and the Unitary Group*.

**Remark (the configuration of the two involutions).** A complex vector space with a conjugation and a Hermitian form carries the three operators $J$, $c$ and the adjoint $\dagger$, with the relations $J^2 = -\mathrm{id}$, $c^2 = \mathrm{id}$, $Jc = -cJ$, and the compatibilities of $J$ and $c$ with $h$; the adjoint of $J$ is $J^{\dagger} = -J$ (the complex structure is skew-adjoint for $h$) and a conjugation $c$ compatible with $h$ is antiunitary, $h(cx,cy) = \overline{h(x,y)}$, self-adjoint in the antilinear sense. These are the linear relations that the operators of the category satisfy, and they are the model of the operator theory of the later group.

## The Transport of the Real Structure to the Endomorphism Algebra

**Proposition (the conjugation of operators).** The conjugation $c$ acts on the endomorphism algebra by
$$
c\cdot X = cXc \qquad (X \in \operatorname{End}_{\mathbb C}(V)),
$$
and this is a $\mathbb{C}$-linear algebra automorphism of order two, whose fixed subalgebra is the complexification of the endomorphisms of the real form,
$$
\operatorname{End}_{\mathbb C}(V)^{c} \cong \operatorname{End}_{\mathbb R}(V_0)\otimes_{\mathbb R}\mathbb{C} = \operatorname{End}_{\mathbb C}(V_0\otimes_{\mathbb R}\mathbb C).
$$

**Proof.** The map $X\mapsto cXc$ is $\mathbb C$-linear because $c$ is antilinear and appears twice, $cXc(\lambda v) = cX(\bar\lambda cv) = c(\bar\lambda Xcv) = \lambda cXcv$; it is an algebra automorphism and an involution because $c^2 = \mathrm{id}$. An operator is fixed, $cXc = X$, exactly when $X$ commutes with $c$, that is when $X$ preserves $V_0$ and is the complexification of its real restriction; the $\mathbb{R}$-linear endomorphisms of $V_0$ complexify to the $\mathbb C$-linear endomorphisms of $V = V_0\otimes\mathbb C$ commuting with $c$.

**Proposition (the conjugate-linear companion and the adjoint).** If $h$ is compatible with $c$, the map
$$
X \longmapsto c\,X^{\dagger}\,c
$$
is a conjugate-linear algebra anti-automorphism of order two, and it is the transport of the real structure to the algebra; the two maps together make the endomorphism algebra an algebra with a real structure and an involution, whose fixed part is $\operatorname{End}_{\mathbb R}(V_0)$.

**Proof.** The adjoint $\dagger$ is conjugate-linear and an anti-automorphism, and $c$ is conjugate-linear, so the composite $X\mapsto cX^{\dagger}c$ is conjugate-linear and an anti-automorphism; its square is $c(cX^{\dagger}c)^{\dagger}c = c\,cX\,c\,c = X$. The fixed elements are the operators with $cX^{\dagger}c = X$, which for $X$ commuting with $c$ and self-adjoint is the real endomorphism. This is *Real Structures on the Operator Layer* and *The Adjoint of a Hermitian Operator*, the latter later in this category.

## Summary

On a complex vector space $V$ of dimension $m$ the complex structure $J$ and a conjugation $c$ satisfy $J^2 = -\mathrm{id}$, $c^2 = \mathrm{id}$ and $Jc = -cJ$, generating $\mathrm{Cl}_{1,1}\cong M_2(\mathbb R)$, and the fixed set $V_0 = \operatorname{Fix}(c)$ is a totally real real form with $V = V_0\oplus JV_0$; the companion $K = Jc$ is a second conjugation, and $c$ and $K$ agree exactly for a $J$-stable real form. A Hermitian form $h$ compatible with $c$, $h(cx,cy) = \overline{h(x,y)}$, restricts to a real symmetric positive-definite form on $V_0$, and the decomposition $h = g - i\omega$ has $g$ symmetric $J$-invariant and $\omega$ alternating with $\omega(x,Jy) = g(x,y)$; the signature of the restriction is the unitary invariant of the compatible conjugation. The conjugation transports to the endomorphism algebra as the $\mathbb C$-linear involution $X\mapsto cXc$, whose fixed part is the complexification of $\operatorname{End}_{\mathbb R}(V_0)$, and as the conjugate-linear anti-automorphism $X\mapsto cX^{\dagger}c$, the adjoint companion; these are the linear relations behind the operator theory of the later group. The manifold forms are *Real Structures on a Complex Manifold* and *Complex Manifolds with an Antiholomorphic Involution*; the Hermitian forms and the unitary group are *Hermitian Geometry and the Unitary Group*; the operator layer is *Real Structures on the Operator Layer*; the Clifford algebra is *Clifford Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$, $J^2=-\mathrm{id}$ | the complex structure |
| $c$, $c^2=\mathrm{id}$, $c(iv)=-ic(v)$ | the conjugation, a conjugate-linear involution |
| $Jc=-cJ$ | the anticommutation, the $\mathrm{Cl}_{1,1}$ relations |
| $V_0=\operatorname{Fix}(c)$ | the real form, totally real, $V=V_0\oplus JV_0$ |
| $K=Jc$ | the companion conjugation |
| $h(cx,cy)=\overline{h(x,y)}$ | compatibility of $c$ with the Hermitian form |
| $h=g-i\omega$ | real part symmetric, imaginary part alternating |
| $X\mapsto cXc$, $X\mapsto cX^{\dagger}c$ | the transport to the endomorphism algebra |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for conjugate-linear maps, real structures and descent.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the complex structure operator, the adjoint and Hermitian forms.
- Werner Greub, *Linear Algebra* (Springer, fourth edition, 1975), for the real and complex structures on a real vector space and the decompositions they induce.
- Robert Silhol, *Real Algebraic Surfaces* (Lecture Notes in Mathematics 1399, Springer, 1989), for real structures on complex vector spaces and the real forms.
