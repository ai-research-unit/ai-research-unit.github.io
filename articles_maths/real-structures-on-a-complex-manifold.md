
# __Real Structures on a Complex Manifold__

## Introduction

A **real structure** on a complex manifold $M$ is an antiholomorphic involution
$$
c : M \longrightarrow M, \qquad c^2 = \mathrm{id}, \qquad dc\circ J = -J\circ dc ,
$$
the manifold form of complex conjugation. Its fixed set
$$
M^{c} = \{ p \in M : c(p) = p \}
$$
is the set of **real points**, and it is the real locus of the geometry that $c$ selects: the complex conjugation on $\mathbb{C}^n$ has $M^c = \mathbb{R}^n$, the conjugation on the projective space has $M^c = \mathbb{RP}^n$, and on a general complex manifold the real points are, when nonempty, a smooth real-analytic submanifold of real dimension $n$ — a real form or a union of real forms — and can be empty. A real structure makes the manifold the complexification of its real points in the good case: the holomorphic tangent vector at a real point, an element of a complex vector space of dimension $n$, is the complexification of the real tangent space of the fixed submanifold, and the fields defined over the reals are the fields fixed by the transport along $c$. The article studies the involution and the real points; the quotient by the involution and the classification of the real structures up to isomorphism, the **real forms**, are the companion article *Complex Manifolds with an Antiholomorphic Involution*.

The article has three sections: the antiholomorphic involution and the conjugation; the real points; and the real structure as a descent datum. The real structure on a smooth manifold and the real stack of a real manifold are *Real Structures on a Smooth Manifold*; the complex structure, the almost complex operator and the type are *Hermitian Geometry and Almost Complex Structures* and *The Almost Complex Operator*; the linear model on a complex vector space is *The Involution on a Complex Vector Space*, later in this category; the real structures on an algebraic variety and the Galois descent are *Real Structures on Varieties and Galois Descent*. None of that is re-derived. The Riemannian case, in which the real structure is required to preserve the metric, is *Real Structures on a Riemannian Manifold*, earlier in this Part.

Throughout, $M$ is a connected complex manifold of complex dimension $n$, $J$ is its complex structure, $c : M \to M$ is a real structure, $M^{c}$ is the set of real points, $T^{1,0}M$ and $T^{0,1}M$ are the holomorphic and antiholomorphic tangent bundles, and $\mathbb{C}^n$ and $\mathbb{CP}^n$ carry their standard real structures.

## The Antiholomorphic Involution and the Conjugation

**Definition.** A **real structure** on the complex manifold $M$ is an involutive diffeomorphism $c$ with
$$
c^2 = \mathrm{id}, \qquad dc_p \circ J_p = -J_{c(p)} \circ dc_p \quad (p \in M),
$$
that is an antiholomorphic involution; the pair $(M, c)$ is a **complex manifold with a real structure**. A map $F : (M, c) \to (N, d)$ of two such manifolds is **real** when $F \circ c = d \circ F$ and **holomorphic** when it is complex-linear for the two complex structures.

**Proposition (the conjugation reverses the type).** The differential of a real structure exchanges the two eigenbundles of $J$,
$$
dc\bigl(T^{1,0}M\bigr) = T^{0,1}M, \qquad dc\bigl(T^{0,1}M\bigr) = T^{1,0}M ,
$$
and pulls a $(p,q)$-form back to a $(q,p)$-form, $c^{*}\Omega^{p,q}(M) \subseteq \Omega^{q,p}(M)$; on the level of the operators it conjugates the complex structure, $dc\circ J = -J\circ dc$, and it maps the Cauchy–Riemann operator $\bar\partial$ to $\partial$, $c^{*}\circ\bar\partial = \partial\circ c^{*}$.

**Proof.** From $dc\circ J = -J\circ dc$ the differential carries the $+i$ eigenspace of $J$ to the $+i$-eigenspace of $-J = \bar J$..., which is the $-i$ eigenspace of $J$, that is $T^{0,1}M$; the type of a form is the number of holomorphic and antiholomorphic legs, and exchanging the two bundles exchanges $p$ and $q$. The Cauchy–Riemann statement is the reality of the decomposition $d = \partial + \bar\partial$: conjugating a $\bar\partial$-closed form gives a $\partial$-closed form. The type decomposition is *Operators on a Complex Manifold*.

**Proposition (the linear model).** On $\mathbb{C}^n$ the **standard real structure** is the componentwise complex conjugation
$$
c(z) = \bar z, \qquad c(z_1,\dots,z_n) = (\bar z_1,\dots,\bar z_n),
$$
and on $\mathbb{CP}^n$ the standard real structure is $c([z_0:\dots:z_n]) = [\bar z_0:\dots:\bar z_n]$; both are antiholomorphic involutions, and their real points are $\mathbb{R}^n$ and $\mathbb{RP}^n$.

**Proof.** Complex conjugation is $\mathbb{R}$-linear, involutive, and satisfies $\bar\imath = -i$; hence it is antiholomorphic; it descends to the projective space because it commutes with the scalar action of $\mathbb{C}$, and its fixed points in $\mathbb{C}^n$ are the real points $\mathbb{R}^n$, while in $\mathbb{CP}^n$ the fixed points are the classes that can be represented by real vectors, that is $\mathbb{RP}^n$. The linear model is *The Involution on a Complex Vector Space* and *Complex Subspaces*.

**Remark (the two faces of $c$).** The real structure is a real geometric object and acts on every structure the manifold carries: on the tangent bundle it is the transport that pairs a holomorphic direction with an antiholomorphic one, on the forms it is the conjugation, and on the functions it is the operation $f \mapsto \bar f\circ c$ that conjugates values. A holomorphic function on $(M,c)$ is real when $\bar f\circ c = f$; a holomorphic form is real when its class is fixed by $c^{*}$, and this is the real form of a complex object, which the companion article develops.

## The Real Points

**Proposition (the real points of a real structure).** The real points $M^{c} = \operatorname{Fix}(c)$ form a closed real submanifold or a disjoint union of submanifolds of $M$; at a real point $p$ the tangent space splits as
$$
T_pM = T_pM^{c} \oplus J_p\,T_pM^{c}
$$
where $T_pM^{c}$ is the $+1$-eigenspace of $dc_p$ and $J_pT_pM^{c}$ is the $-1$-eigenspace, so that $T_pM$ is the complexification of the real tangent space of the real locus and $T_pM^{c}$ is totally real, $T_pM^{c}\cap J_pT_pM^{c} = 0$.

**Proof.** At a fixed point $p$ the differential $dc_p$ is an $\mathbb{R}$-linear involution with $dc_pJ = -Jdc_p$; its $+1$-eigenspace is the tangent space of the fixed submanifold in the sense of the standard fixed-submanifold theorem, and its $-1$-eigenspace is $J$ applied to it, since $dc_p(Jv) = -Jdc_p(v)$; hence $T_pM = T_pM^c\oplus J T_pM^c$. The closedness of the fixed set is the continuity of $c$, and the smoothness of the component through a point with $dc_p$ having no eigenvalue other than $\pm1$ is the regular-value theorem.

**Proposition (the real locus has dimension $n$ or is empty).** If $M^{c}$ is nonempty then at every real point $p$ the $+1$-eigenspace $T_pM^{c}$ of $dc_p$ has real dimension exactly $n$ and is totally real, so $M^{c}$ is a real-analytic submanifold of real dimension $n$, possibly with several components; the real locus can also be empty.

**Proof.** The differential $dc_p$ is an $\mathbb{R}$-linear involution of the real $2n$-dimensional space $T_pM$ with $dc_pJ = -Jdc_p$; if $v$ is fixed then $Jv$ is negated, and conversely, so $J$ maps the $+1$-eigenspace isomorphically onto the $-1$-eigenspace and the two have equal dimension $n$, with zero intersection. The fixed set is then a real-analytic submanifold of dimension $n$ at each of its points, by the standard fixed-submanifold theorem, and its components may be several. Examples at the two extremes: the conjugation $z\mapsto\bar z$ on $\mathbb{C}^n$ has the real locus $\mathbb{R}^n$ of dimension $n$, and the real structure $c(z) = -1/\bar z$ on $\mathbb{CP}^1$ has fixed equation $z\bar z = -1$, so its real locus is empty.

**Corollary (the real form).** When the real locus $M^{c}$ is nonempty, the condition $T_pM = T_pM^{c}\otimes_{\mathbb R}\mathbb C$ for every $p$ is automatic, so $M^c$ is a **real form** of $M$; the manifold $M$ is the **complexification** of the real manifold $M^c$ when moreover a neighbourhood of $M^c$ exhausts $M$, and then a real structure whose fixed set is $M^c$ is exactly the datum of the real form.

**Proof.** The identification $T_pM = T_pM^c\otimes_{\mathbb R}\mathbb C$ is the split of the previous proposition; it is an isomorphism of complex vector spaces because $J$ acts on $J T_pM^c$ by $-\mathrm{id}$ when $T_pM^c$ is identified with its complexification through $J$. The complexification of a real manifold $N$ is a complex manifold of complex dimension $n$ with the real structure $c$ whose fixed set is $N$, and the descent is the assignment of the real objects. This is *Real Structures on a Smooth Manifold* and *Real Structures on Varieties and Galois Descent*.

## The Real Structure as a Descent Datum

**Definition.** Let $(M, c)$ be a complex manifold with a real structure. A **real structure on a structure** of $M$ (a metric, a form, a bundle, an operator) is a data on $M$ fixed by the transport along $c$; when the real locus is a real form $N = M^{c}$, the objects fixed by $c$ are the **descended** objects of $N$, and the assignment is **descent** along the real structure.

**Proposition (the descent).** The holomorphic objects fixed by the real structure are the complexifications of the real objects of the real form $N$; the assignment is an equivalence of categories between the real objects of $N$ and the $c$-fixed holomorphic objects of $M$, and it sends the real forms of a complex object to the original objects of $N$.

**Proof.** On the complexification $M = N_{\mathbb C}$ the transport $\bar{}$ on the coefficients is the conjugation, and a holomorphic function $f$ satisfies $\bar f \circ c = f$ exactly when its Taylor coefficients are real, that is when it is the complexification of a real-analytic function on $N$; the same argument for the sections of a bundle with a real structure. This is the descent of *Real Structures on Varieties and Galois Descent*, in the real-analytic and differentiable setting.

**Example (the projective conjugation and the real structure of a lattice).** On $\mathbb{CP}^{n}$ the standard conjugation has real points $\mathbb{RP}^n$ and descends the real objects of the real projective space: the real linear forms on $\mathbb C^{n+1}$ fixed by the conjugate of the standard real structure give the real forms of the projective space, and the real structure on the tautological bundle descends to the tautological bundle of $\mathbb{RP}^n$. This is the model in which the real structure of the complex manifold and the real structure of its linear data are the two ends of the same descent, and it is *Real Structures on a Projective Space*.

**Remark (the two readings of a real structure).** Read forward, the real structure is an involution of $M$ with real points; read backward, it is the datum that makes $M$ the complexification of a real manifold and a real structure the descent of a real geometry. The two readings agree when $M$ is the complexification of its real locus and separate otherwise: a real structure with empty real points, such as a fixed-point-free conjugation, is a genuine involution of $M$ but descends no real manifold in the naive sense. The quotient of $M$ by such an involution, and the classification of the real structures up to isomorphism, are the subject of *Complex Manifolds with an Antiholomorphic Involution*.

## Summary

A real structure on a complex manifold $M$ is an antiholomorphic involution $c$, $dc\circ J = -J\circ dc$, the manifold form of complex conjugation; it exchanges the holomorphic and antiholomorphic tangent bundles, sends $\Omega^{p,q}$ to $\Omega^{q,p}$, and conjugates $\bar\partial$ to $\partial$. Its real points $M^{c}$ are, when nonempty, a real-analytic submanifold of real dimension $n$ — a union of real forms — and at each real point $T_pM = T_pM^{c}\oplus J T_pM^{c}$ with $T_pM^c$ the $+1$-eigenspace of $dc_p$, of dimension $n$ and totally real, so that at a real point the tangent space is the complexification of the real tangent space; the real locus can also be empty. When $M$ is the complexification of its real locus, the holomorphic objects fixed by $c$ are the complexifications of the real objects, which is the descent datum. The standard models are the conjugation $z\mapsto\bar z$ on $\mathbb{C}^n$ with real points $\mathbb{R}^n$ and the classwise conjugation on $\mathbb{CP}^n$ with real points $\mathbb{RP}^n$. The real structure on a smooth manifold is *Real Structures on a Smooth Manifold*, the linear model is *The Involution on a Complex Vector Space*, the descent is *Real Structures on Varieties and Galois Descent*, and the quotient and the real forms are *Complex Manifolds with an Antiholomorphic Involution*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c$ | the real structure, $c^2=\mathrm{id}$, antiholomorphic |
| $dc\circ J=-J\circ dc$ | the conjugate-linearity of the differential |
| $M^{c}=\operatorname{Fix}(c)$ | the real points |
| $T_pM = T_pM^{c}\oplus J T_pM^{c}$ | the split of the tangent space at a real point |
| $N = M^{c}$ | the real form (dimension $n$ when nonempty) |
| $c^{*}$ | the conjugation of forms, exchanging $(p,q)$ and $(q,p)$ |

## Further Reading

- Robert Silhol, *Real Algebraic Surfaces* (Lecture Notes in Mathematics 1399, Springer, 1989), for real structures, their real loci and the real forms of a complex surface.
- Klaus Fritzsche and Hans Grauert, *From Holomorphic Functions to Complex Manifolds* (Springer, 2002), for complex conjugation, real points and antiholomorphic involutions on complex manifolds.
- Robert C. Gunning and Hugo Rossi, *Analytic Functions of Several Complex Variables* (Prentice-Hall, 1965), for conjugation, real forms and the fixed-point sets of antiholomorphic involutions.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for involutions, fixed-point sets and the quotient by an involution.
