# __Reduced Biquaternion Integration__

## Introduction

This article develops the integral theory of the reduced biquaternion algebra: the integral of an algebra-valued function on a domain, the integration by parts, the divergence theorem and Green's formulas, the fundamental solution of the reduced Cauchy–Riemann operator, the Cauchy integral formula and its consequences, and the residue theory. It follows *Reduced Biquaternion Regular Functions*, where the operator and its regular functions are studied. Because the algebra is **commutative**, no left-versus-right bookkeeping is needed and the vector identities take their ordinary form, against the two non-commutative members of the family. The treatment is purely mathematical.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, and $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The squared Euclidean norm is $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$, the algebra is identified with $\mathbb{R}^{4}$ by the coordinate isometry $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$, and the Lebesgue measure of that identification is written $\mathrm{d}\mu$. A reduced-analytic function is $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ with $G_{1},G_{2}$ holomorphic.

## The Integral of a Reduced-Biquaternion-Valued Function

**Definition.** For a domain $\Omega$ and a Bochner-measurable $f:\Omega\to\mathbb{B}_{\mathrm{r}}$, the **integral** $\int_{\Omega}f\,\mathrm{d}\mu$ is the element whose four real coordinates are the integrals of the four coordinate functions. The space $L^{1}(\Omega)$ consists of the $f$ with $\int_{\Omega}\lVert f\rVert\,\mathrm{d}\mu<\infty$, where $\lVert f\rVert=\sqrt{K(f)}$.

**Theorem (linearity, additivity and the estimate).** The integral is $\mathbb{R}$-linear, additive on disjoint domains, and satisfies
$$
\Bigl\lVert\int_{\Omega}f\,\mathrm{d}\mu\Bigr\rVert\le\int_{\Omega}\lVert f\rVert\,\mathrm{d}\mu .
$$
It reduces in the idempotent coordinates to the pair of complex integrals,
$$
\int_{\Omega}f\,\mathrm{d}\mu=\Bigl(\int_{\Omega}g_{1}\,\mathrm{d}\mu\Bigr)\Pi_++\Bigl(\int_{\Omega}g_{2}\,\mathrm{d}\mu\Bigr)\Pi_-.
$$

*Proof.* The four coordinates are ordinary Lebesgue integrals, so every statement about them is the corresponding statement for real functions; the idempotent decomposition is a linear isomorphism and the coordinates $g_{1},g_{2}$ are the two characters, which are continuous linear functionals, so they pass through the integral; the estimate is the triangle inequality for the Euclidean norm applied to the vector of the four coordinate integrals.

## Integration by Parts

**Theorem (the derivative of an integral and integration by parts).** For a $C^{1}$ function $f$ on a bounded $\Omega$ with piecewise smooth boundary, and any coordinate direction with unit vector $e_{\nu}$,
$$
\int_{\Omega}\partial_{\nu}f\,\mathrm{d}\mu=\int_{\partial\Omega}f\,n_{\nu}\,\mathrm{d}S ,
$$
the outward normal $n=(n_{q_{\blacktriangle}},n_{q'_{\blacktriangle}},n_{q_{\blacktriangledown}},n_{q'_{\blacktriangledown}})$ and $\mathrm{d}S$ the surface measure. Consequently, for $C^{1}$ functions $f,h$,
$$
\int_{\Omega}(\partial_{\nu}f)\,h\,\mathrm{d}\mu=-\int_{\Omega}f\,(\partial_{\nu}h)\,\mathrm{d}\mu+\int_{\partial\Omega}f\,h\,n_{\nu}\,\mathrm{d}S .
$$

*Proof.* The scalar divergence theorem applied to each of the four real coordinates of $f$ gives the first display; the product rule $\partial_{\nu}(fh)=(\partial_{\nu}f)h+f\partial_{\nu}h$ holds because the algebra is **commutative** and the derivative is a derivation, and integrating the product rule and applying the divergence theorem gives the second display.

**Corollary (no side bookkeeping).** Since the multiplication is commutative, the two displays above hold without any distinction between a left and a right gradient, in contrast with the split biquaternion case, where transposing the gradient off a product requires the right gradient $\overleftarrow{\nabla}$.

*Proof.* The product rule and the divergence theorem are identities in the commutative algebra, and no ordering convention is needed.

## The Divergence Theorem

**Definition.** For a $C^{1}$ field $f$ the **divergence** is $\operatorname{div}f=\partial/\partial q_{\blacktriangle}f_{q_{\blacktriangle}}+\partial/\partial q'_{\blacktriangle}f_{q'_{\blacktriangle}}+\partial/\partial q_{\blacktriangledown}f_{q_{\blacktriangledown}}+\partial/\partial q'_{\blacktriangledown}f_{q'_{\blacktriangledown}}$ when $f$ is resolved into its four coordinate components, and the **algebra-valued divergence** is
$$
\operatorname{Div}f=\sum_{\nu=1}^{4}\partial_{\nu}f\,\otimes\,e_{\nu},
$$
the sum of the four partial derivatives, which is the gradient of the algebra-valued field read in the monomial basis.

**Theorem (the divergence theorem).** For a $C^{1}$ field $f$ on a bounded domain with piecewise smooth boundary,
$$
\boxed{\;
\int_{\Omega}\operatorname{Div}f\,\mathrm{d}\mu=\int_{\partial\Omega}f\,n\,\mathrm{d}S
\;},
$$
where $f n$ is the algebra product of the boundary value and the outward normal read in the algebra.

*Proof.* Apply the scalar divergence theorem to each coordinate component and reassemble in the algebra basis; the boundary integrand is the outer product of the boundary value and the normal, which in the commutative algebra is unambiguous.

## Green's Formulas

**Theorem (Green's first and second formulas).** For $C^{1}$ reduced biquaternion fields $f,h$ on a bounded domain,
$$
\int_{\Omega}\bigl((\partial f)\!\cdot\!(\partial h)+f\,\Delta h\bigr)\mathrm{d}\mu=\int_{\partial\Omega}f\,(\partial/\partial n\,h)\,\mathrm{d}S ,
$$
$$
\int_{\Omega}\bigl(f\,\Delta h-h\,\Delta f\bigr)\mathrm{d}\mu=\int_{\partial\Omega}\bigl(f\,\partial/\partial n\,h-h\,\partial/\partial n\,f\bigr)\mathrm{d}S ,
$$
where $\partial f\cdot\partial h=\sum_{\nu}(\partial_{\nu}f)(\partial_{\nu}h)$ is the Euclidean pairing of the two gradients, $\Delta$ is the Euclidean Laplacian and $\partial/\partial n$ the normal derivative.

*Proof.* Green's first formula is the divergence theorem applied to the field $f\,\nabla h$, whose divergence is $(\nabla f)\cdot(\nabla h)+f\Delta h$ by the product rule and the commutativity; the second is the first with the roles exchanged, subtracted, the bilinear terms cancelling.

**Corollary (harmonicity again).** For reduced-analytic $f,h$ the volume terms vanish, $\Delta f=\Delta h=0$, so $\int_{\Omega}(f\Delta h-h\Delta f)\mathrm{d}\mu=0$ and the boundary integral is zero: the reduced biquaternion version of Green's second formula is the ordinary one for harmonic functions.

*Proof.* Every reduced-analytic function is harmonic by *Reduced Biquaternion Regular Functions*, §*Harmonicity and the Factorization of the Laplacian*.

## The Fundamental Solution

**Definition.** The **Cauchy kernel** is
$$
G(\breve Q)=\frac{1}{2\pi i}\Bigl(\frac{\Pi_+}{Q_{+}}+\frac{\Pi_-}{Q_{-}}\Bigr).
$$
The fundamental solution of $\partial/\partial\bar Q_{+}$ in the $Q_{+}$-plane is $1/(\pi Q_{+})$, and $G$ is $(2i)^{-1}$ times its two-factor lift.

**Theorem (the distributional identity and its limit).** In the $Q_{+}$-plane, with $Q_{-}$ held as a parameter,
$$
\partial/\partial\bar Q_{+}\,\Bigl(\frac{1}{\pi Q_{+}}\Bigr)=\delta ,
$$
the two-dimensional Dirac measure at the origin of that plane, and symmetrically for $Q_{-}$. The kernel $G$ is therefore $(2i)^{-1}$ times a fundamental solution of $\partial/\partial\bar Q_{+}$ **transversally**, on each of the two coordinate planes, and it is locally integrable on the algebra with the singular set $Z=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$ removed.

**Remark (the honest limits).** A single four-dimensional fundamental solution in the classical sense does not exist, because the singular set $Z$ is a union of two planes of real codimension two, not a point: the delta in the identity above is the two-dimensional delta of one coordinate plane, the normal directions to that plane carrying no singularity. This is the analytic form of the fact that the operator is elliptic at no point, and it is why the integral theory is a **pair** of one-variable theories rather than a four-dimensional one. On the two planes the algebra is not invertible, and the kernel is undefined there.

## The Cauchy Integral Formula

**Theorem (Cauchy's theorem).** Let $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ be reduced-analytic on a domain, and let $\gamma_{1}$ and $\gamma_{2}$ be closed contours in the $Q_{+}$-plane and the $Q_{-}$-plane, swept out by a curve in the algebra on which $f$ is regular. Then
$$
\boxed{\;
\oint f\,\mathrm{d}\breve Q=0
\;},
$$
the differential being $\mathrm{d}\breve Q=\mathrm{d}Q_{+}\,\Pi_++\mathrm{d}Q_{-}\,\Pi_-$ along the curve.

*Proof.* The integral splits in the idempotent coordinates into $\Pi_+\oint_{\gamma_{1}}G_{1}(Q_{+})\mathrm{d}Q_{+}+\Pi_-\oint_{\gamma_{2}}G_{2}(Q_{-})\mathrm{d}Q_{-}$, each a one-variable contour integral of a holomorphic function, which vanishes by the classical Cauchy theorem.

**Theorem (the Cauchy integral formula).** Let $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ be reduced-analytic on a domain containing the point $\breve Q_{0}$ with coordinates $Q_{0+},Q_{0-}$, and let $\gamma_{1},\gamma_{2}$ be simple closed contours encircling $Q_{0+}$ and $Q_{0-}$ counterclockwise, on which $f$ is regular. Then
$$
\boxed{\;
f(\breve Q_{0})=\frac{1}{2\pi i}\Bigl(\Pi_+\oint_{\gamma_{1}}\frac{G_{1}(Q_{+})}{Q_{+}-Q_{0+}}\,\mathrm{d}Q_{+}+\Pi_-\oint_{\gamma_{2}}\frac{G_{2}(Q_{-})}{Q_{-}-Q_{0-}}\,\mathrm{d}Q_{-}\Bigr)
\;}.
$$

*Proof.* In each idempotent component the classical Cauchy integral formula gives $G_{1}(Q_{0+})=(2\pi i)^{-1}\oint G_{1}(Q_{+})/(Q_{+}-Q_{0+})\mathrm{d}Q_{+}$ and the companion for $G_{2}$; multiplying by the idempotents and adding gives the display, and the two contours are independent, one in each complex coordinate plane.

**Corollary (the boundary form is cylindrical).** The formula is a pair of one-variable formulas, so the value at $\breve Q_{0}$ is reproduced from the values on the union of the two cylinders over $\gamma_{1}$ and $\gamma_{2}$, not from a single three-dimensional boundary in the algebra. The order of the two integrations is immaterial.

*Proof.* Each contour lives in one coordinate plane and its cylinder is the product of that plane curve with the other complex coordinate; the two terms add in the idempotent coordinates.

## Consequences of the Cauchy Integral Formula

**Analyticity.** A reduced-analytic function has the two holomorphic components $G_{1},G_{2}$, so it is real-analytic and all its derivatives are regular; the $n$-th derivative is obtained by differentiating the kernel, $G_{1}^{(n)}(Q_{0+})\Pi_++G_{2}^{(n)}(Q_{0-})\Pi_-$.

**The mean value property.** Each component satisfies the one-variable mean value property, and since the Euclidean Laplacian is the ordinary one in four real variables, a reduced-analytic function has the mean value property over the Euclidean balls of the algebra.

**Liouville's theorem.** A reduced-analytic function bounded on the whole algebra is constant: $G_{1}$ depends on $Q_{+}$ alone and is bounded as $Q_{+}$ ranges over $\mathbb{C}$, so it is constant by the one-variable Liouville theorem, and $G_{2}$ likewise.

**The maximum principle.** A non-constant reduced-analytic function has no interior maximum of $\lVert f\rVert$ on a connected domain, because each component is harmonic for the ordinary Laplacian.

*Proof.* All four statements are the classical ones applied in each coordinate, using the harmonicity of the components and their holomorphy in one variable; the boundedness on the whole algebra forces the boundedness of each component on the whole coordinate plane.

## The Residue Theory

**Theorem (the residue theorem).** Let $f$ be meromorphic in each coordinate, regular off the poles, with poles $Q_{p+}$ in the $Q_{+}$-plane and $Q_{q-}$ in the $Q_{-}$-plane. Then for contours encircling the appropriate poles,
$$
\oint f\,\mathrm{d}\breve Q=2\pi i\Bigl(\Pi_+\sum_{p}\operatorname{Res}_{Q_{p+}}G_{1}+\Pi_-\sum_{q}\operatorname{Res}_{Q_{q-}}G_{2}\Bigr),
$$
the two sums being the ordinary one-variable residues.

*Proof.* The integral splits as before, and the classical residue theorem applied to each holomorphic component gives the two sums.

**Corollary (the residue at a higher-order pole).** If $G_{1}$ has a pole of order $m$ at $Q_{0+}$ with Laurent expansion $\sum_{r\ge-m}c_{r}(Q_{+}-Q_{0+})^{r}$, the residue is $c_{-1}$, given by $\operatorname{Res}_{Q_{0+}}G_{1}=(m-1)!^{-1}\lim_{Q_{+}\to Q_{0+}}\frac{\mathrm{d}^{m-1}}{\mathrm{d}Q_{+}^{m-1}}\bigl((Q_{+}-Q_{0+})^{m}G_{1}(Q_{+})\bigr)$; the same formula holds in the $Q_{-}$-coordinate. The two contributions are independent and add in the idempotent coordinates.

*Proof.* The residue of a pole of order $m$ is the coefficient of $(Q_{+}-Q_{0+})^{-1}$ in the Laurent expansion, and the displayed formula extracts it by differentiation.

## The Role of the Zero Divisors

**The kernel is local.** The Cauchy kernel has its singularities on the two lines $Q_{+}=0$ and $Q_{-}=0$, the union $Z$, and the contours of the Cauchy and residue theorems must avoid $Z$; since $Z$ has codimension two, a contour in either coordinate plane can be shrunk around a point without meeting $Z$ unless the point itself lies on the line.

**The characteristic set is the union of the two cylinders.** The one-variable Cauchy theory requires the derivative to be inverted off the pole; on the algebra the inverse of the operator is available only after the two coordinates are separated, and the failure of the inverse on $Z$ is the failure of the difference quotient there.

**Integration along the algebra itself.** A curve in the four-dimensional algebra not lying in a coordinate plane does not reduce to the product of two one-variable contours, and the integral along it is not directly given by the classical theory; the reduced biquaternion integration is therefore developed on the two coordinate planes and lifted by the idempotents, and the general four-dimensional boundary form is not available.

## The Relation to Complex and Quaternionic Analysis

The reduced biquaternion integral theory is the pair of the one-variable complex theories, one in $Q_{+}$ and one in $Q_{-}$: the Cauchy theorem, the Cauchy integral formula, the consequences and the residue theorem all reduce to their classical counterparts in the two coordinates. The commutative multiplication removes the left-versus-right distinction of the split biquaternion and biquaternion cases, where Green's formulas must be stated with both gradients. Against the quaternion and biquaternion cases, where the Cauchy kernel $Q_{\mathrm{ts}}/\lVert Q\rVert_{E}^{4}$ is a genuine fundamental solution of a first-order operator in four real variables, the reduced case has no single four-dimensional fundamental solution, the operator being elliptic nowhere and its singular set being a union of two codimension-two planes; the integral theory therefore remains a two-factor theory, in the same way as the regularity theory. The integral theory of the split biquaternion case, the two quaternion halves, is the exact structural analogue with $\mathbb{H}$ in place of $\mathbb{C}$.

## Summary

The integral of a reduced biquaternion-valued function on a domain of $\mathbb{R}^{4}$ is defined coordinatewise with respect to the Lebesgue measure; it is linear and additive and satisfies the fundamental estimate, and it splits in the idempotent coordinates into the pair of complex integrals. Integration by parts, the divergence theorem and Green's formulas hold in their ordinary forms, with no left-versus-right bookkeeping, because the algebra is commutative; for reduced-analytic functions they reduce to the identities for harmonic functions. The Cauchy kernel $G(\breve Q)=(2\pi i)^{-1}(\Pi_+/Q_{+}+\Pi_-/Q_{-})$ is the lift of the one-variable kernel $1/(\pi Q_{+})$ of $\partial/\partial\bar Q_{+}$, and it is a fundamental solution transversally on each coordinate plane; a single four-dimensional fundamental solution does not exist, because the singular set $Z=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$ has codimension two and the operator is elliptic nowhere. The Cauchy theorem gives $\oint f\,\mathrm{d}\breve Q=0$ for reduced-analytic $f$, and the Cauchy integral formula reproduces $f(\breve Q_{0})$ from the two one-variable contour integrals over the contours encircling $Q_{0+}$ and $Q_{0-}$; analyticity, the mean value property, Liouville's theorem and the maximum principle follow from the classical theory in each coordinate. The residue theorem reduces to the two one-variable residue theorems, with the poles located on the two coordinate lines. The whole theory is the pair of the complex one-variable theories lifted by the idempotents, against the single non-commutative theory of the biquaternion case and the two quaternion halves of the split biquaternion case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\int_{\Omega}f\,\mathrm{d}\mu$ | Integral of an algebra-valued function on a domain |
| $\lVert f\rVert=\sqrt{K(f)}$ | Euclidean norm of the value |
| $\operatorname{Div}f=\sum_{\nu}\partial_{\nu}f\otimes e_{\nu}$ | Algebra-valued divergence |
| $\Delta$ | Euclidean Laplacian in the four real coordinates |
| $G(\breve Q)=\tfrac{1}{2\pi i}(\Pi_+/Q_{+}+\Pi_-/Q_{-})$ | Cauchy kernel |
| $1/(\pi Q_{+})$ | One-variable fundamental solution of $\partial/\partial\bar Q_{+}$ |
| $\oint f\,\mathrm{d}\breve Q=0$ | Cauchy theorem for reduced-analytic $f$ |
| $f(\breve Q_{0})=\tfrac{1}{2\pi i}(\Pi_+\oint\frac{G_{1}}{Q_{+}-Q_{0+}}\mathrm{d}Q_{+}+\Pi_-\oint\frac{G_{2}}{Q_{-}-Q_{0-}}\mathrm{d}Q_{-})$ | Cauchy integral formula |
| $\operatorname{Res}_{Q_{0+}}G_{1}$ | One-variable residue in the $Q_{+}$-coordinate |
| $Z=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$ | Zero-divisor set |

## Further Reading

- Lars V. Ahlfors, *Complex Analysis*, 3rd edition (McGraw-Hill, 1979), for the Cauchy theorem, the Cauchy integral formula and the residue theorem in one variable.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for the Cauchy integral formula and the Cauchy kernel in the non-commutative hypercomplex setting.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the divergence theorem, Green's formulas and the fundamental solution of the hypercomplex operator.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the contour integrals and the Cauchy theory of the commutative multicomplex calculus.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the integral representation of the holomorphic functions of the idempotent algebra.
