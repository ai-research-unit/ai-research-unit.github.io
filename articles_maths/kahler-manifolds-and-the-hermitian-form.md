
# __Kähler Manifolds and the Hermitian Form__

## Introduction

A **Kähler manifold** is a complex manifold with a Hermitian metric whose associated $(1,1)$-form is closed: the Hermitian form $h = g - i\omega$ of the chapter, split into its real part $g$ and its imaginary part $\omega$, has imaginary part
$$
\omega(X, Y) = g(JX, Y)
$$
which is a real $2$-form of type $(1,1)$, and the metric is Kähler when $d\omega = 0$. The closedness is the compatibility of the Hermitian form with the complex structure of the manifold: it is equivalent to the almost complex structure being parallel for the metric, $\nabla J = 0$, and to the Kähler form being parallel, $\nabla\omega = 0$, so that the holonomy of the metric preserves the complex structure and the geometry is at once complex, Riemannian and symplectic. The closedness has an analytic consequence of the first importance, the **Kähler identities**
$$
[\Lambda, \partial] = -i\,\bar\partial^{*}, \qquad [\Lambda, \bar\partial] = i\,\partial^{*}, \qquad [\Lambda, d] = d^{*},
$$
which express the adjoints of the Cauchy–Riemann operators through the contraction with the Kähler form and give the equality of the three Laplacians $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$; the identities are the operator form of the closedness, and the Hodge decomposition of a compact Kähler manifold is their consequence.

The article has three sections: the Kähler condition and the closedness; the Kähler identities; and the Hermitian form, the positivity and the Kähler cone. The Hermitian metrics, the fundamental form, the Chern connection and the type decomposition are *Hermitian Geometry and Almost Complex Structures*, *Hermitian Metrics and the Levi-Civita Connection* and *Operators on a Complex Manifold*; the complex manifolds and their complex structure are *Complex Manifolds* and *Hermitian Geometry and Almost Complex Structures*; the Lefschetz operator, the contraction and the Hodge–Riemann relations are *The Kähler Form Operator*, earlier in this category, which quotes the identities proved here; the Laplace operators and the Hodge theory are *The Codifferential*, *Hermitian Metrics and the Codifferential* and *Hermitian Metrics and the Hodge Theory*, the last in *Geometry on Rings and Fields*; the symplectic structure carried by $\omega$ is *Symplectic Geometry* and *Symplectic Manifolds*; the curvature of the Kähler metric is *The Curvature Operator of a Complex Manifold*. None of that is re-derived.

Throughout, $(M, J, g)$ is a complex manifold of complex dimension $n$ with a Hermitian metric, $h = g - i\omega$ is the Hermitian form, $\omega(X,Y) = g(JX,Y)$ is the **Kähler form**, $L(\alpha) = \omega\wedge\alpha$ is the Lefschetz operator, $\Lambda = L^{*}$ is the contraction, $\partial$ and $\bar\partial$ are the Cauchy–Riemann operators with formal adjoints $\partial^{*}$, $\bar\partial^{*}$ for the metric, and $\Delta_d = d d^{*} + d^{*}d$, $\Delta_\partial = \partial\partial^{*}+\partial^{*}\partial$, $\Delta_{\bar\partial} = \bar\partial\bar\partial^{*}+\bar\partial^{*}\bar\partial$ are the Laplacians.

## The Kähler Condition and the Closedness

**Definition.** A Hermitian metric $g$ on a complex manifold is **Kähler** when its associated form $\omega$ is closed, $d\omega = 0$; the manifold with a Kähler metric is a **Kähler manifold**, and $\omega$ is its **Kähler form**.

**Proposition (the equivalent conditions).** For a Hermitian metric $g$ on a complex manifold $(M, J)$ the following are equivalent:
$$
d\omega = 0, \qquad \nabla\omega = 0, \qquad \nabla J = 0, \qquad \nabla^{\mathrm{C}}J = J\nabla^{\mathrm C},
$$
where $\nabla$ is the Levi-Civita connection, $\nabla^{\mathrm C}$ the Chern connection and $\nabla^{\mathrm C}J$ is the covariant derivative of the tensor $J$. Each says that the complex structure of the manifold is parallel for the metric, so that the Riemannian holonomy is contained in the unitary group.

**Proof.** $d\omega$ is a $3$-form of type $(2,1)\oplus(1,2)$, and the $(2,1)$-part is the Nijenhuis-type obstruction $\nabla\omega$ evaluated on holomorphic vectors up to a nonzero factor: the identity $d\omega = 0$ is equivalent to $\nabla\omega = 0$ because the metric is Hermitian and the connection is the Levi-Civita one, which is torsion-free; $\nabla\omega = 0$ is equivalent to $\nabla J = 0$ because $\omega(X,Y) = g(JX,Y)$ and $g$ is parallel; finally $\nabla^{\mathrm C}J = 0$ is the statement that the Chern connection is the Levi-Civita connection, which happens exactly when $\omega$ is closed. The Chern connection $1$-form and the torsion are *Hermitian Metrics and the Levi-Civita Connection*. This is *Kähler Geometry*.

**Proposition (the local potential and the integrability).** On a Kähler manifold every point has a neighbourhood with a real function $\varphi$, the **Kähler potential**, such that
$$
\omega = i\,\partial\bar\partial\varphi ;
$$
and conversely a real function with $i\partial\bar\partial\varphi$ positive definite defines a Kähler metric. In particular the Kähler form is closed as a form of type $(1,1)$, and the Kähler metric is at once Kähler and a symplectic structure on the underlying real manifold.

**Proof.** $d\omega = 0$ with $\omega$ of type $(1,1)$ is the local $\partial\bar\partial$-lemma: a closed form of type $(1,1)$ is locally $\partial\bar\partial$ of a real function, by the Poincaré lemma for $\partial$ and $\bar\partial$; the positivity of $i\partial\bar\partial\varphi$ is the positive definiteness of the Hermitian form. The symplectic structure is the closedness and the nondegeneracy of $\omega$, which is the positive definiteness of $g$ through $\omega(X,JX) = g(X,X) > 0$. The $\partial\bar\partial$-lemma and the forms are *Hodge Theory*, and the symplectic structure is *Symplectic Geometry*.

**Remark (the three structures).** The Kähler condition is the compatibility of the three structures a Hermitian manifold carries: the complex structure $J$, the Riemannian metric $g$, and the symplectic form $\omega$. A Kähler manifold is a complex manifold, a Riemannian manifold and a symplectic manifold at once, and the three are linked by $g(X,Y) = \omega(X,JY)$ and $\omega(X,Y) = g(JX,Y)$; the closedness of $\omega$ is exactly the condition that the symplectic structure be compatible with the complex one. This is the sense in which the Hermitian form of the chapter is the object that the Kähler condition selects among the Hermitian metrics.

## The Kähler Identities

**Theorem (the Kähler identities).** On a Kähler manifold the contractions and the Cauchy–Riemann operators satisfy
$$
[\Lambda, \partial] = -i\,\bar\partial^{*}, \qquad [\Lambda, \bar\partial] = i\,\partial^{*}, \qquad [\Lambda, d] = d^{*} .
$$
The last is the sum of the first two, $[\Lambda, d] = [\Lambda,\partial]+[\Lambda,\bar\partial] = d^{*}$.

**Proof.** Work at a point $p$ in holomorphic normal coordinates, so that $\partial_k g_{j\bar l}(p) = 0$ and $\omega = i\sum_k dz_k\wedge d\bar z_k$ at $p$ to the relevant order. The operators of exterior multiplication and contraction satisfy the Clifford relations, and the Leibniz rule for $\Lambda$ against $\partial$ and $\bar\partial$ reduces at $p$ to the commutation of $\Lambda$ with the holomorphic and anti-holomorphic derivations; the computation gives $[\Lambda,\partial] = -i\bar\partial^{*}$ and, by conjugation, $[\Lambda,\bar\partial] = i\partial^{*}$. The normal coordinates exist because the metric is Kähler, which is the only place where $d\omega = 0$ enters; the Clifford relations of the exterior algebra and its contraction are *The Kähler Form Operator* and *The Volume Element, Duality and the Hodge Star*.

**Corollary (the equality of the Laplacians).** On a Kähler manifold
$$
\Delta_d = 2\,\Delta_\partial = 2\,\Delta_{\bar\partial} ,
$$
and consequently the harmonic forms for the three Laplacians coincide; the bidegree operators and the Cauchy–Riemann operators preserve the harmonic space, and on a compact Kähler manifold the de Rham cohomology decomposes as $H^{k}(M;\mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}$ with $H^{p,q} = \overline{H^{q,p}}$.

**Proof.** From $[\Lambda,\partial] = -i\bar\partial^{*}$ and its adjoint, one has $\bar\partial^{*} = i[\Lambda,\partial]$; substituting into $\Delta_{\bar\partial}$ and using the Jacobi identity for the three operators gives $\Delta_{\bar\partial} = \Delta_\partial$ and $\Delta_d = 2\Delta_{\bar\partial}$. Since $\Delta_\partial$ preserves the bidegree, the harmonic forms acquire a bigrading, and by the Hodge theorem on a compact manifold the cohomology inherits it. The Hodge theorem is *Hermitian Metrics and the Hodge Theory* and *Hodge Theory*.

**Remark (the operator content).** The Kähler identities are the operator form of the closedness of the Kähler form: in them the contraction $\Lambda$, which is the adjoint of the Lefschetz operator, is the mediator between the Cauchy–Riemann operators and their adjoints, and the equality of the Laplacians is the statement that the complex geometry and the real geometry have the same harmonic theory. This is the sense in which the Kähler identities are the central computation of the category, and why every operator of the category is read against them.

## The Hermitian Form, the Positivity and the Kähler Cone

**Proposition (positivity of the Kähler form).** The Kähler form $\omega$ is a **positive** $(1,1)$-form: for every nonzero real tangent vector $v$,
$$
\omega(v, Jv) = g(v, v) > 0 ,
$$
and for a complex line $T \subseteq T_pM$ spanned in a unitary frame by the real vectors $u, Ju$ one has $\omega(u,Ju) = |u|^2 > 0$; the form is thus positive in the sense of positivity of the associated Hermitian form $h = g - i\omega$.

**Proof.** $\omega(v,Jv) = g(Jv,Jv) = g(v,v)$ by the compatibility $g(JX,JY) = g(X,Y)$ and $J^2 = -\mathrm{id}$; the positivity of $g$ gives the strict inequality. The evaluation on the complex line is the same computation in a frame adapted to $T$. Positivity of the Hermitian form and of the $(1,1)$-form is *Hermitian Geometry and Almost Complex Structures*.

**Definition.** On a compact Kähler manifold the **Kähler cone** is the open convex cone
$$
\mathcal{K} = \{ [\omega] \in H^{1,1}(M;\mathbb{R}) : [\omega]\ \text{is the class of a Kähler form} \},
$$
the set of cohomology classes representable by positive closed $(1,1)$-forms; a manifold is **Kähler** when its Kähler cone is nonempty.

**Proposition (the Kähler cone is open and convex).** The Kähler cone is an open convex cone in the real vector space $H^{1,1}(M;\mathbb R)$, and it contains the class of the Kähler form; the sum of a Kähler class and a positive $(1,1)$-class is a Kähler class, so the cone is convex, and the positivity is open in the space of classes.

**Proof.** If $\omega_1$ and $\omega_2$ are Kähler then $(1-t)\omega_1 + t\omega_2$ is closed, of type $(1,1)$, and positive for every $t \in [0,1]$ because a positive combination of positive forms is positive; hence the cone is convex. Openness is the openness of the positive definiteness in the space of $(1,1)$-classes with a fixed representative. This is *Kähler Geometry* and *Symplectic Manifolds*.

**Example (the flat, the Hopf and the projective cases).** On $\mathbb{C}^n$ with the Euclidean metric the Kähler form is $\omega = \frac{i}{2}\sum_k dz_k\wedge d\bar z_k$, closed because the coefficients are constant, and the metric is flat. On the torus $\mathbb{C}^n/\Lambda$ the same form descends to a flat Kähler form. The Hopf surface is a compact complex surface with no Kähler metric, so its Kähler cone is empty: the closedness of the associated form fails for every Hermitian metric, and the operator Kähler identities fail with it. On $\mathbb{CP}^n$ the Fubini–Study form is the Kähler form of the standard metric, positive and closed, and its class generates the Kähler cone; this is the model in which the Hermitian form of the chapter, the Kähler form, the symplectic form and the complex structure are the same object read four ways.

## Summary

A Kähler manifold is a complex manifold with a Hermitian metric whose associated form $\omega(X,Y) = g(JX,Y)$ of type $(1,1)$ is closed, $d\omega = 0$; this is equivalent to $\nabla\omega = 0$, to the parallelism $\nabla J = 0$ of the complex structure, and to the Chern connection being the Levi-Civita connection, and locally it is the existence of a Kähler potential with $\omega = i\partial\bar\partial\varphi$. The Kähler form is positive, $\omega(v,Jv) = g(v,v) > 0$, so the metric is at once complex, Riemannian and symplectic. The closedness has the operator form of the Kähler identities $[\Lambda,\partial] = -i\bar\partial^{*}$, $[\Lambda,\bar\partial] = i\partial^{*}$, $[\Lambda,d] = d^{*}$, which give the equality of the Laplacians $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$ and, on a compact manifold, the Hodge decomposition of the de Rham cohomology into the bigraded pieces $H^{p,q}$. The Kähler cone is the open convex cone of the classes representable by Kähler forms; it is nonempty exactly for a Kähler manifold, and the Hopf surface is its standard counterexample. The Hermitian form, the fundamental form and the type decomposition are *Hermitian Geometry and Almost Complex Structures*, *Hermitian Metrics and the Levi-Civita Connection* and *Operators on a Complex Manifold*; the Lefschetz operator and the Hodge–Riemann relations are *The Kähler Form Operator*; the Hodge theory is *Hermitian Metrics and the Hodge Theory*; the symplectic structure is *Symplectic Geometry*; the curvature is *The Curvature Operator of a Complex Manifold*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h=g-i\omega$ | the Hermitian form, real part the metric, imaginary part the Kähler form |
| $\omega(X,Y)=g(JX,Y)$ | the Kähler form |
| $d\omega=0$ | the Kähler condition |
| $\nabla J=0$ | the parallelism of the complex structure |
| $\omega=i\partial\bar\partial\varphi$ | the local Kähler potential |
| $[\Lambda,\partial]=-i\bar\partial^{*}$, $[\Lambda,\bar\partial]=i\partial^{*}$ | the Kähler identities |
| $\Delta_d=2\Delta_\partial=2\Delta_{\bar\partial}$ | the equality of the Laplacians |
| $\mathcal K\subseteq H^{1,1}(M;\mathbb R)$ | the Kähler cone |

## Further Reading

- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the Kähler condition, the Kähler identities and the Hodge theory.
- Andrei Moroianu, *Lectures on Kähler Geometry* (Cambridge University Press, 2007), for the equivalences of the Kähler condition, the Kähler potential and the Laplacians.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Kähler identities, the Hodge decomposition and the positivity of the Kähler form.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry* (Open Access, 2012), for the Kähler cone, the positivity of $(1,1)$-classes and the $\partial\bar\partial$-lemma.
