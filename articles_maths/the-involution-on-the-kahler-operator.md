
# __The Involution on the Kähler Operator__

## Introduction

On a compact Kähler manifold the Kähler form $\omega$ acts on the exterior algebra by the **Kähler operator**
$$
L : \Omega^{\bullet}(M) \longrightarrow \Omega^{\bullet}(M), \qquad L\alpha = \omega\wedge\alpha,
$$
the Lefschetz operator, with formal adjoint the contraction $\Lambda = L^{*}$; the pair $L,\Lambda$ is the operator face of the Kähler form, and the involution of the title is the pair of natural involutions of the exterior algebra that exchange $L$ with $\Lambda$. The first is the **Hodge star** $\star$, defined by the metric and the orientation, an isometry of the exterior algebra with
$$
\star^{2} = (-1)^{k(2n-k)}\,\mathrm{id} \quad \text{on } \Omega^{k}, \qquad \star L = \Lambda\star , \qquad \star\Lambda = L\star ;
$$
the second is the **complex conjugation** of forms, the map $\sigma(\alpha) = \bar\alpha$ exchanging the bidegrees $(p,q)$ and $(q,p)$, a conjugate-linear involution that commutes with $L$ and $\Lambda$ because the Kähler form is real. Their composite $C = \star\sigma$ (the "conjugate Hodge star") is the involution of the Kähler operator proper: it is the conjugation that carries the Lefschetz operator to the contraction,
$$
C\,L\,C^{-1} = \Lambda, \qquad C\,\Lambda\,C^{-1} = L,
$$
the operator form of the self-adjointness of the Lefschetz operator with respect to the Hermitian inner product $(\alpha,\beta) = \int_M\alpha\wedge\star\bar\beta$, and the reason the $\mathfrak{sl}_2$-structure of the cohomology is a symmetric structure.

The article has three sections: the Kähler operator and its adjoint; the Hodge star and the complex conjugation, and their composite, as the involution that exchanges $L$ and $\Lambda$; and the Hermitian inner product and the self-adjointness of the pair. The Kähler form, the Lefschetz operator, the $\mathfrak{sl}_2$-relations and the Hodge–Riemann relations are *The Kähler Form Operator*, earlier in this category, and *Kähler Manifolds and the Hermitian Form*; the Hodge star, the volume element and the codifferential are *The Volume Element, Duality and the Hodge Star* and *Hermitian Metrics and the Codifferential*; the type decomposition and the Cauchy–Riemann operators are *Operators on a Complex Manifold*; the Hermitian inner product and the self-adjointness are *The Adjoint of a Hermitian Operator*, the first article of this group. None of that is re-derived.

Throughout, $(M,\omega)$ is a compact Kähler manifold of complex dimension $n$ and real dimension $2n$, $L(\alpha) = \omega\wedge\alpha$, $\Lambda = L^{*}$ is the contraction, $\star$ is the Hodge star of the metric and the orientation, $\sigma(\alpha) = \bar\alpha$ is the complex conjugation of forms, and $(\alpha,\beta) = \int_M\alpha\wedge\star\bar\beta$ is the Hermitian inner product.

## The Kähler Operator and Its Adjoint

**Proposition (the Lefschetz operator is self-adjoint for the pairing).** The contraction $\Lambda$ is the formal adjoint of $L$,
$$
(L\alpha,\beta) = (\alpha,\Lambda\beta),
$$
and with $H = [L,\Lambda]$ the three operators satisfy $[H,L] = 2L$, $[H,\Lambda] = -2\Lambda$, $[L,\Lambda] = H$, so that the exterior algebra is a finite-dimensional representation of the Lie algebra $\mathfrak{sl}_2$; on the $k$-forms $H = (k-n)\,\mathrm{id}$.

**Proof.** The metric gives the formal adjoint of exterior multiplication by the Kähler form as contraction with the metric-dual $(1,1)$-vector, which is $\Lambda$; the $\mathfrak{sl}_2$-relations are the standard commutator computation for the operators of exterior multiplication and contraction with a positive $(1,1)$-form, and the eigenvalue of the central element on $k$-forms is $k-n$. This is *The Kähler Form Operator*.

**Remark (the operator and its dual).** The pair $(L,\Lambda)$ is the Kähler operator and its adjoint; the involution of the next sections is the transformation of the exterior algebra that exchanges the two, so that the Kähler geometry of a form is invariant under the exchange. This is the operator content of the symmetry $L\leftrightarrow\Lambda$ of the Lefschetz decomposition.

## The Hodge Star, the Complex Conjugation and the Involution

**Proposition (the Hodge star).** The Hodge star is an isometry of the exterior algebra, $\star^{2} = (-1)^{k(2n-k)}\mathrm{id}$ on the $k$-forms, and it intertwines the Lefschetz operator and the contraction,
$$
\star L = \Lambda\star, \qquad \star\Lambda = L\star .
$$

**Proof.** The identity $\star L = \Lambda\star$ is the classical pairing of exterior multiplication with contraction through the star, with the sign convention of the Hodge star fixed as in *The Volume Element, Duality and the Hodge Star*; it holds on a Kähler manifold because $\omega$ is parallel and the star is built from the metric and the volume element. Applying $\star^{2}$ to both sides and cancelling the scalar $(-1)^{k(2n-k)}$ gives the second identity. The Hodge star and its properties are *The Volume Element, Duality and the Hodge Star*, and the Kähler intertwining is *The Kähler Form Operator*.

**Proposition (the complex conjugation).** The complex conjugation of forms $\sigma(\alpha) = \bar\alpha$ is a conjugate-linear involution of the exterior algebra, $\sigma^{2} = \mathrm{id}$, it exchanges the bidegrees, $\sigma(\Omega^{p,q}) = \Omega^{q,p}$, it is an isometry up to the conjugation of the scalar, $(\sigma\alpha,\sigma\beta) = \overline{(\alpha,\beta)}$, and it commutes with the Kähler operator and the contraction,
$$
\sigma L = L\sigma, \qquad \sigma\Lambda = \Lambda\sigma,
$$
because the Kähler form is real, $\bar\omega = \omega$ and $L$ commutes with $\sigma$ up to the reality of $\omega$.

**Proof.** The conjugation of a form is the conjugation of its coefficients in a real frame; it is conjugate-linear, involutive and exchanges the type; the reality of $\omega$ gives $\sigma(\omega\wedge\alpha) = \omega\wedge\sigma\alpha$, so $\sigma L = L\sigma$, and the conjugate-linearity with the metric (real) gives $\sigma\Lambda=\Lambda\sigma$. The type decomposition is *Operators on a Complex Manifold*.

**Theorem (the involution on the Kähler operator).** The composite $C = \star\sigma$ is an involution up to sign on each degree,
$$
C^{2} = (-1)^{k(2n-k)}\,\mathrm{id}\quad\text{on }\Omega^{k},
$$
and it exchanges the Kähler operator and its adjoint,
$$
C\,L\,C^{-1} = \Lambda, \qquad C\,\Lambda\,C^{-1} = L .
$$

**Proof.** $C^{2} = \star\sigma\star\sigma$; the star is real, so it commutes with the conjugation $\sigma$, and $\sigma^{2}=\mathrm{id}$, giving $C^{2} = \star^{2}$, which is $(-1)^{k(2n-k)}$ on $\Omega^{k}$; and $C L C^{-1} = \star\sigma L\sigma^{-1}\star^{-1} = \star L\star^{-1} = \Lambda$ using $\sigma L = L\sigma$ and $\star L = \Lambda\star$. The inverse $\star^{-1}$ is $\pm\star$, absorbed in the sign. This is *The Kähler Form Operator* and *The Volume Element, Duality and the Hodge Star*.

## The Hermitian Inner Product and the Self-Adjointness

**Proposition (the Hermitian inner product of forms).** The formula
$$
(\alpha,\beta) = \int_{M}\alpha\wedge\star\bar\beta
$$
is a positive-definite Hermitian inner product on the complex-valued forms, and it is invariant under the Hodge star and conjugate-invariant under the complex conjugation; the formal adjoints $d^{*}$, $\partial^{*}$, $\bar\partial^{*}$ are the adjoints of $d$, $\partial$, $\bar\partial$ for it.

**Proof.** The wedge with the star of the conjugate is the metric pairing against the volume element, positive definite because the metric is positive; the star is an isometry, and the conjugation is an antiunitary involution by the previous proposition. The formal adjoints are *The Codifferential* and *Hermitian Metrics and the Codifferential*.

**Corollary (the symmetry of the Kähler structure).** The map $C = \star\sigma$ is the involution under which the Kähler operator and the contraction are exchanged, and it is self-adjoint for $(\cdot,\cdot)$ up to sign; the Lefschetz decomposition and the Hodge–Riemann form are invariant under $C$, which is why the Kähler cohomology is symmetric in the passage from $L$ to $\Lambda$ and from $(p,q)$ to $(n-p,n-q)$.

**Proof.** The first assertion is the theorem; the invariance of the decomposition follows from the commutation relations and the definition of primitive forms, and the symmetry of the Hodge–Riemann form is the $\mathfrak{sl}_2$-symmetry. This is *The Kähler Form Operator*.

**Example (the Riemann surface).** For $n = 1$ the exterior algebra of a Riemann surface has the forms $1, dz, d\bar z, dz\wedge d\bar z$; the star satisfies $\star 1 = dz\wedge d\bar z$ and acts on the $(1,0)$- and $(0,1)$-forms by $\pm i$, and $C = \star\sigma$ exchanges $L$ (multiplication by the area form) with $\Lambda$ (contraction), so the involution is the Poincaré duality of the surface read through the complex conjugation. On $\mathbb{CP}^n$ the same involution exchanges the powers $L^{k}$ and $\Lambda^{k}$ of the Lefschetz and contraction operators, giving the symmetry of the Hodge numbers and the hard Lefschetz theorem.

## Summary

On a compact Kähler manifold the Kähler operator $L(\alpha) = \omega\wedge\alpha$ has the contraction $\Lambda = L^{*}$ for its adjoint, and the pair satisfies the $\mathfrak{sl}_{2}$-relations $[H,L]=2L$, $[H,\Lambda]=-2\Lambda$ with $H = [L,\Lambda] = (k-n)\mathrm{id}$ on $k$-forms. The Hodge star is an isometry with $\star^{2} = (-1)^{k(2n-k)}$ on $\Omega^{k}$ and intertwines $\star L = \Lambda\star$, $\star\Lambda = L\star$; the complex conjugation $\sigma(\alpha) = \bar\alpha$ is a conjugate-linear involution exchanging the bidegrees and commuting with $L$ and $\Lambda$. Their composite $C = \star\sigma$, an involution up to sign on each degree, exchanges the Kähler operator and its adjoint, $CLC^{-1} = \Lambda$ and $C\Lambda C^{-1} = L$, and it is the symmetry of the Hermitian inner product $(\alpha,\beta) = \int\alpha\wedge\star\bar\beta$ under which the Lefschetz decomposition and the Hodge–Riemann form are invariant. The Kähler operator and the $\mathfrak{sl}_2$-relations are *The Kähler Form Operator* and *Kähler Manifolds and the Hermitian Form*; the Hodge star is *The Volume Element, Duality and the Hodge Star*; the type decomposition is *Operators on a Complex Manifold*; the self-adjointness is *The Adjoint of a Hermitian Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L(\alpha)=\omega\wedge\alpha$ | the Kähler (Lefschetz) operator |
| $\Lambda=L^{*}$ | the contraction |
| $[H,L]=2L$, $[H,\Lambda]=-2\Lambda$ | the $\mathfrak{sl}_2$-relations, $H=(k-n)\mathrm{id}$ on $k$-forms |
| $\star^{2}=(-1)^{k(2n-k)}$ on $\Omega^{k}$ | the Hodge star, an isometry |
| $\star L=\Lambda\star$, $\star\Lambda=L\star$ | the intertwining |
| $\sigma(\alpha)=\bar\alpha$ | the complex conjugation, exchanging $(p,q)$ |
| $C=\star\sigma$ | the involution, $CLC^{-1}=\Lambda$ |

## Further Reading

- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Lefschetz operators, the Hodge star and the Hodge–Riemann relations.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the Lefschetz operator, the contraction and the $\mathfrak{sl}_2$-structure.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry* (Open Access, 2012), for the Hodge star, the complex conjugation of forms and the Hermitian inner product.
- Andrei Moroianu, *Lectures on Kähler Geometry* (Cambridge University Press, 2007), for the Kähler operator, its adjoint and the symmetry of the Lefschetz decomposition.
