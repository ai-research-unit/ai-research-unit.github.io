
# __Split-Quaternion Analysis__

## Introduction

This article treats the analysis of functions of a split-quaternion variable. It records the metric and topological structure, defines limits and continuity, explains why the naive derivative fails, presents the differential operators of the system and identifies their type, treats power series, and describes the singularities caused by the zero divisors.

The split-quaternion algebra, its norm form, its matrix model and its idempotents are assumed from *Split-Quaternion Algebra*; the units and the zero divisors from *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Zero Divisors*; the metric and the geometry of the forms from *Split-Quaternion Geometry*. The analytic theory of the division-algebra case is that of *Quaternion Analysis*, and of the two-dimensional hyperbolic case that of *Split-Complex Integration*; the differential operators of the definite (Clifford) case are those of *Clifford Analysis*, *Dirac Operators* and *Regularity and the Cauchy–Riemann Operator*. Nothing physical is invoked.

## The Metric Structure

**Definition.** Identify $\mathbb{H}_{\mathrm{s}}$ with $\mathbb{R}^4$ by $x = a + b e_1 + c e_2 + d e_3$, and put

$$
|x|^2 = a^2 + b^2 + c^2 + d^2 .
$$

This is the **Euclidean norm** of the algebra. The norm form $N(x) = a^2 + b^2 - c^2 - d^2$ is indefinite and is not a norm.

**Theorem (The Algebra Is a Normed Algebra up to a Constant).** For all $x,y \in \mathbb{H}_{\mathrm{s}}$,

$$
|x y| \leq \sqrt{2}\,|x|\,|y| .
$$

The map $\Phi$ to $M_2(\mathbb{R})$ satisfies $|\Phi(x)|_{\mathrm{F}} = \sqrt{2}\,|x|$, where $|\cdot|_{\mathrm{F}}$ is the Frobenius norm; the Euclidean norm induces the product topology of $\mathbb{R}^4$.

**Proof.** Write $\Phi(x) = \begin{pmatrix} a-d & c-b \\ b+c & a+d\end{pmatrix}$. Then

$$
|\Phi(x)|_{\mathrm{F}}^2 = (a-d)^2 + (c-b)^2 + (b+c)^2 + (a+d)^2 = 2a^2 + 2b^2 + 2c^2 + 2d^2 = 2|x|^2 .
$$

The Frobenius norm is submultiplicative, $|\Phi(x)\Phi(y)|_{\mathrm{F}} \leq |\Phi(x)|_{\mathrm{F}}|\Phi(y)|_{\mathrm{F}}$, so $\sqrt{2}|xy| \leq 2|x||y|$ and the bound follows. The topology statement is the identification of $\mathbb{R}^4$ with the Frobenius-normed matrix space, which preserves the topology. $\square$

**Corollary (Open and Closed Sets).** The group of units is open, the zero divisor set is closed, and the unit group is a topological group in the Euclidean topology. The norm-one group $U$ and the norm-form level sets are closed subsets.

**Proof.** The units are $\{N \neq 0\}$, the complement of the closed level set $N = 0$; the zero divisors are $\{x \neq 0, N(x)=0\} \cup \{0\}$, the intersection of a closed set with a closed set; the group operations are continuous by the bound, and the level sets are closed because $N$ is continuous. $\square$

**Corollary (No Multiplicative Norm).** There is no norm on the algebra satisfying $|xy| = |x||y|$ for all $x,y$.

**Proof.** Such a norm would force $x \neq 0 \neq y \Rightarrow xy \neq 0$, which fails for the zero divisors of *Split-Quaternion Zero Divisors*. $\square$

## Limits and Continuity

**Definition.** A function $f : \mathbb{H}_{\mathrm{s}} \to \mathbb{H}_{\mathrm{s}}$ has **limit** $L$ at $x_0$ when for every $\varepsilon > 0$ there is $\delta > 0$ with $|f(x)-L| < \varepsilon$ whenever $0 < |x - x_0| < \delta$; and $f$ is **continuous** at $x_0$ when the limit there is $f(x_0)$.

**Theorem (Continuity of the Algebraic Operations).** The maps $(x,y) \mapsto x+y$, $(x,y)\mapsto xy$, $x \mapsto \lambda x$, $x\mapsto \bar{x}$, $x \mapsto \operatorname{Sc}(x)$ and $x \mapsto \operatorname{Vec}(x)$ are continuous on $\mathbb{H}_{\mathrm{s}}$, and $x \mapsto x^{-1}$ is continuous on the open set of units.

**Proof.** The sum and scalar product are linear in the coordinates; the product satisfies $|xy - x_0y_0| \leq |x-x_0||y| + |x_0||y-y_0|$ for the coordinate norm up to a constant, hence is continuous; the involutions and the projections are linear in the coordinates. For the inverse, $x^{-1}-x_0^{-1} = x^{-1}(x_0-x)x_0^{-1}$ and $x \mapsto x^{-1}$ is bounded near $x_0$ by the continuity of the coordinates of the inverse, which are rational functions of the coordinates with denominator $N(x)$. $\square$

**Corollary (Entrywise Description).** Continuity, limits and convergence of sequences in the algebra are equivalent to the corresponding statements for the four matrices entries of the matrix model $\Phi$.

**Proof.** The map $\Phi$ is a homeomorphism onto its image with the topology of the Frobenius norm, and all norms on a finite-dimensional space are equivalent. $\square$

## The Naive Derivative and Why It Fails

**Definition.** The **naive derivative** of $f$ at $x$ is the limit of the difference quotients

$$
\lim_{h \to 0} \big(f(x+h)-f(x)\big) h^{-1}, \qquad \lim_{h \to 0} h^{-1}\big(f(x+h)-f(x)\big),
$$

when the limits exist; the first is the left quotient and the second is the right quotient, and they differ in general because the algebra is not commutative.

**Theorem (The Naive Derivative Fails Already for Squares).** For $f(x) = x^2$ and every $x$,

$$
\big(f(x+h)-f(x)\big) h^{-1} = x + h x h^{-1} + h
$$

for every invertible $h$, and the quotient depends on $h$ unless $x$ is central. Consequently $x^2$ has no naive derivative at any point, and the only functions with a naive derivative on an open set are built from central elements.

**Proof.** Expand: $(x+h)^2 - x^2 = xh + hx + h^2$, and $(xh)h^{-1} = x$, $h^2h^{-1} = h$, so the display follows. The quotient depends on $h$ through $h x h^{-1}$, which is the conjugate of $x$ by $h$; by (*Split-Quaternion Algebra*, §*Conjugations and Fixed-Point Subspaces*) this varies with $h$ unless $x$ is central. If a naive derivative exists at every point of an open set then $x \mapsto x^2$ would have to be differentiable there, which it is not. $\square$

**Corollary (The Obstruction Is the Non-Commutativity, Not the Zero Divisors).** The failure displayed is due to the non-commutativity of the algebra; the zero divisors add a second obstruction, because the difference quotient requires $h$ invertible and the invertible elements do not contain a neighbourhood of every point of the interior of the zero divisor set.

**Proof.** The first statement is the computation; the second is the definition of the zero divisor set and the openness of the units. $\square$

**Conclusion.** The naive derivative is not the right notion on this algebra. The replacement is the operator calculus of the next section, in the tradition of Clifford analysis, together with the entrywise calculus transported from the matrix model.

## The Differential Operators

**Definition.** With the coordinates $x = a + b e_1 + c e_2 + d e_3$, the **vector operator** of the system is

$$
D = e_1 \frac{\partial}{\partial b} + e_2 \frac{\partial}{\partial c} + e_3 \frac{\partial}{\partial d},
$$

acting on functions of the four coordinates, and the **scalar** derivative is $\partial_a = \partial/\partial a$.

**Theorem (The Square of the Operator Is the Wave Operator).** Using $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$ and $e_ie_j = -e_je_i$ for $i \neq j$,

$$
D^2 = -\frac{\partial^2}{\partial b^2} + \frac{\partial^2}{\partial c^2} + \frac{\partial^2}{\partial d^2} = \Box_{(2,1)},
$$

the wave operator of the form of signature $(2,1)$, which is hyperbolic. The first-order operator $D$ itself is not elliptic: its symbol is left multiplication by the frequency vector, invertible exactly when $N \neq 0$, so the set where the symbol degenerates is the null cone

$$
b^2 - c^2 - d^2 = 0 ,
$$

which is the zero divisor set of the algebra in the vector subspace.

**Proof.** Expanding the square, the cross terms cancel because the generators anticommute and the second derivatives commute, and the diagonal terms carry the signs of the squares of the generators; the symbol of $D$ is $e_1 \xi_1 + e_2 \xi_2 + e_3 \xi_3$, whose square is $-\xi_1^2 + \xi_2^2 + \xi_3^2$, vanishing exactly on the null cone. By *Split-Quaternion Zero Divisors*, §*The Zero Divisor Set as the Null Cone*, the null cone of the vector subspace is the zero divisor set. $\square$

**Corollary (No Elliptic Theory).** There is no analogue of the elliptic theory of monogenic functions. Every solution of $Df = 0$ solves the wave equation $\Box_{(2,1)}f = 0$, because $D^2 = \Box_{(2,1)}$, but not conversely: the scalar function $f = bc$ satisfies $\Box_{(2,1)}f = 0$ while $Df = c\,e_1 + b\,e_2 \neq 0$. The monogenic class is therefore a proper subclass of the wave solutions, it is not closed under the operations of the elliptic theory, and its members have neither the mean-value property nor the maximum principle nor the elliptic regularity of *Clifford Analysis*; the zero divisors of the algebra are exactly the characteristic directions of the operator.

**Proof.** The implication is $D^2 = \Box_{(2,1)}$, the counterexample is the displayed computation, and an operator with a cone of nonzero characteristic vectors is not elliptic, so the elliptic-theoretic properties fail along the characteristic directions; the identification of the characteristic variety with the zero divisors is the theorem. That the class is much smaller than the wave solutions, and in particular is not parametrised by arbitrary data on a hypersurface, is the kernel computation of *Split-Quaternion Integration*, §*The Kernel of the Vector Operator*, where the two transported families and the nonzero compactly supported solutions are exhibited. The elliptic case is *Clifford Analysis* and *Regularity and the Cauchy–Riemann Operator*. $\square$

**Corollary (The Operators on the Algebra and on the Vector Subspace).** The operator $D$ acts on functions whose variable lies in the vector subspace, or on the vector part of a function of the full algebra. The operator associated with the full form of signature $(2,2)$ is the Clifford operator of the algebra $\mathrm{Cl}_{2,2}$, whose generators are not the generators $e_1,e_2,e_3$ of $\mathbb{H}_{\mathrm{s}}$ alone; the two operators are different, and the analysis of the full algebra is not the analysis of its vector part.

**Proof.** The generators of $\mathbb{H}_{\mathrm{s}}$ have the sign pattern $(-,+,+)$ and span a three-dimensional subspace, so they generate the Clifford algebra of the restricted form, not of the form on the algebra; the operator of the (2,2) form requires four anticommuting generators. $\square$

**Remark (One Variable and Several Variables).** In the one-variable tradition of *Quaternion Analysis* the derivative is taken with respect to the full variable and the operator is the Dirac operator of the ambient form; in the several-variable tradition of the Part III articles the operator is a fixed first-order system. On this algebra the second reading is the only one available: the first leads to the wave operator above, whose theory is hyperbolic.

## Power Series and Analytic Functions

**Definition.** A **power series** with coefficients in the algebra is a series $\sum_{n \geq 0} c_n x^n$ with $c_n \in \mathbb{H}_{\mathrm{s}}$; it is **absolutely convergent** at $x$ when $\sum |c_n|\,|x|^n$ converges.

**Theorem (Convergence and the Matrix Model).** A power series converges absolutely on the open ball of radius $R = 1/\limsup |c_n|^{1/n}$ and defines a continuous function there; under the matrix model the series converges if and only if each of its four entries converges, and the value is $\Phi^{-1}$ of the entrywise sum. In particular the exponential, the logarithm and the elementary series of *Split-Quaternion Elementary Functions* are defined on their balls of convergence in the entrywise sense.

**Proof.** Absolute convergence follows from the bound $|c_nx^n| \leq (\sqrt{2})^n|c_n||x|^n$, which reduces to the real majorant series; continuity follows from the continuity of the algebraic operations and the entrywise statement from the homeomorphism $\Phi$. $\square$

**Corollary (No Identity Theorem).** Two convergent power series that agree on an open set need not agree on their common domain; the identity theorem fails.

**Proof.** The algebra has zero divisors, so a nonzero element can act as zero on a factor: if $z \neq 0$ has $z^2 = 0$, then the function $x \mapsto z(x - x_0)$ vanishes on the set $x - x_0 \in z\mathbb{H}_{\mathrm{s}}$, which contains a point but not an open set, while $x \mapsto z(x-x_0)^2$ vanishes on a larger set; the standard connectedness argument of the identity theorem requires a product ring with no nilpotents. The failure is the nilpotent phenomenon of *Split-Quaternion Zero Divisors*, §*Nonzero Nilpotents*. $\square$

## Singularities

**Theorem (The Inverse and Its Singular Set).** The function $x \mapsto x^{-1}$ is defined and continuous on the open set of units and has no extension to the null cone. In coordinates, if $x = a + v$ with $v \in V$, then

$$
x^{-1} = \frac{\bar{x}}{N(x)} = \frac{a - v}{a^2 - N(v)},
$$

which blows up as the denominator tends to zero, and the limit depends on the direction of approach: along a null direction the inverse is unbounded, and along the split-complex subalgebra directions the denominator vanishes on the isotropic lines.

**Proof.** The formula for the inverse is that of *Split-Quaternion Algebra*, §*The Norm Form*; the denominator is $N(x)$, which vanishes exactly on the zero divisor set by *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*; the unboundedness along the null directions is immediate from the formula, since the numerator does not vanish there. $\square$

**Corollary (Removable Singularities Fail).** A function that is continuous on the complement of a point of the null cone and bounded near it need not extend across it, because the zero divisors of $x$ make the algebraic operations degenerate along the cone.

**Proof.** The inverse on a sequence approaching a null point along a null direction is unbounded, and other functions built from $x^{-1}$ acquire directional limits; the removable-singularity theorem of one complex variable requires a normed division algebra and fails here. The distributional treatment of the singularities is the subject of *Split-Quaternion Integration*. $\square$

## The Calculus in the Peirce Coordinates

The idempotents of the algebra give coordinates in which the algebraic operations become explicit, and they turn the calculus into an entrywise calculus.

**Definition.** With $u_{\pm} = \tfrac12(1 \pm e_2)$, the **Peirce coordinates** of $x$ are

$$
x = \sum_{\epsilon,\eta \in \{+,-\}} u_\epsilon\, x\, u_\eta,
$$

and the four components $u_\epsilon x u_\eta$ are one-dimensional real subspaces.

**Theorem (The Peirce Coordinates Are the Matrix Entries of the Adapted Model).** The map

$$
x \longmapsto \big(u_+xu_+,\ u_+xu_-,\ u_-xu_+,\ u_-xu_-\big)
$$

is a linear isomorphism of $\mathbb{H}_{\mathrm{s}}$ with the four lines, and the components multiply as the matrix units: for any $x, y$,

$$
(u_\epsilon x u_\eta)(u_{\eta'} y u_{\epsilon'}) = 0 \quad \text{unless } \eta = \eta',
$$

and, when $\eta = \eta'$, the product is $u_\epsilon (x u_\eta y) u_{\epsilon'}$, which lies in the line $u_\epsilon\mathbb{H}_{\mathrm{s}}u_{\epsilon'}$. The coordinates are therefore a presentation of the algebra as a matrix algebra.

Written in the basis $1, e_1, e_2, e_3$, the four components of $x = a + be_1 + ce_2 + de_3$ are

$$
u_+xu_+ = (a+c)\,u_+, \qquad u_-xu_- = (a-c)\,u_-, \qquad u_+xu_- = \tfrac{b-d}{2}(e_1-e_3), \qquad u_-xu_+ = \tfrac{b+d}{2}(e_1+e_3).
$$

The resulting matrix model is the one adapted to the idempotents rather than the model $\Phi$ of *Split-Quaternion Matrix Representations*, §*The Image as a Linear Subspace*: with $P = \begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix}$ one has $\Psi = P\Phi P^{-1}$, and

$$
\Psi(x) = \begin{pmatrix} a+c & b-d \\ -(b+d) & a-c \end{pmatrix},
$$

whose four entries are the four Peirce coordinates. The two models are conjugate by the fixed involution $P$, and the Peirce coordinates are the fixed linear change $(a,b,c,d) \mapsto (a+c,\ a-c,\ b-d,\ b+d)$ of the coordinates of the standard model; they are not the entries of $\Phi$ itself.

**Proof.** The decomposition of the identity $1 = u_+ + u_-$ with $u_+u_- = u_-u_+ = 0$ gives the direct sum, and the dimension count gives one dimension per Peirce space; the vanishing of the mixed products is $u_\eta u_{\eta'} = 0$ for $\eta \neq \eta'$. The displayed components are read off the multiplication table: $u_+u_+ = u_+$, $u_\pm e_2 u_\pm = \pm u_\pm$, $u_+e_1u_+ = u_+e_3u_+ = u_-e_1u_- = u_-e_3u_- = 0$, $u_+e_1u_- = \tfrac12(e_1-e_3)$, $u_+e_3u_- = -\tfrac12(e_1-e_3)$, $u_-e_1u_+ = u_-e_3u_+ = \tfrac12(e_1+e_3)$. For $\Psi$: the map $x \mapsto P\Phi(x)P^{-1}$ is multiplicative because $\Phi$ is, and on the basis it gives $I$, $-J$, $-D$, $-K$, so it is the algebra isomorphism $\Psi$ displayed; its entries are therefore the four Peirce coordinates, and $\Phi(u_+) = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} \neq E_{11}$ shows that the two models differ. $\square$

**Corollary (Partial Derivatives and Smoothness).** A function $f$ of the split-quaternion variable is smooth in the sense of this article exactly when its four Peirce components are smooth functions of the four Peirce coordinates, that is, when its matrix-model entries are smooth; the partial derivatives with respect to the Peirce coordinates are the entries of the matrix-model derivatives, and every operator of the preceding section is a first-order operator with constant coefficients in these coordinates.

**Proof.** The map to the Peirce coordinates is a linear isomorphism, hence a diffeomorphism, and the definition of smoothness is transported along it; the operators have constant coefficients in the coordinates $(a,b,c,d)$ and therefore in the linear coordinates. $\square$

## Comparison with the Quaternion and Split-Complex Cases

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}$ |
|---|---|---|---|
| norm | definite, multiplicative | indefinite, not multiplicative | indefinite, not multiplicative |
| zero divisors | none | the null cone | the isotropic lines |
| naive derivative | fails for squares | fails for squares | fails for squares |
| natural operator | the Dirac operator, elliptic | the wave operator, hyperbolic | the wave operator in one variable |
| characteristic variety | none (elliptic) | the null cone | the isotropic lines |
| regularity | elliptic (monogenic) | hyperbolic, no elliptic regularity | hyperbolic |
| identity theorem | holds on connected domains | fails | fails |

The quaternion column is the content of *Quaternion Analysis*, and the split-complex column that of *Split-Complex Integration*. The single cause of every difference is the presence of zero divisors, equivalently the indefiniteness of the form: the definiteness of the quaternion norm is exactly what makes its Dirac operator elliptic and its analysis regular.

## Summary

The algebra is a normed algebra up to the constant $\sqrt{2}$ in the Euclidean norm, with the product topology of $\mathbb{R}^4$, the units open and the zero divisors closed. Limits and continuity are the entrywise notions of the matrix model. The naive derivative fails already for $x \mapsto x^2$, because the difference quotient involves the conjugate $hxh^{-1}$, and it fails again near the null cone, where $h$ need not be invertible.

The natural operators are the vector operator $D = e_1\partial_b + e_2\partial_c + e_3\partial_d$, whose square is the wave operator of the form of signature $(2,1)$ with characteristic variety the null cone, and the operators of the matrix model. The operator is hyperbolic, so there is no elliptic theory of monogenic functions: the contrast with *Clifford Analysis* is the indefiniteness of the form, and the zero divisors are exactly the characteristic directions. Power series converge on a ball and may be evaluated entrywise, but the identity theorem fails because of the nilpotents. The inverse is given by $\bar{x}/N(x)$ and has its singular set on the null cone, where removable singularities fail. The corresponding analysis of the division-algebra case is that of *Quaternion Analysis*, and of the two-dimensional case that of *Split-Complex Integration*; the operators of the definite case are those of Part III.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $|x|^2 = a^2+b^2+c^2+d^2$ | the Euclidean norm | this article |
| $N(x) = a^2+b^2-c^2-d^2$ | the norm form, indefinite, not a norm | *Split-Quaternion Algebra* |
| $D = e_1\partial_b + e_2\partial_c + e_3\partial_d$ | the vector operator | this article |
| $D^2 = \Box_{(2,1)}$ | the wave operator of signature $(2,1)$ | this article |
| $b^2-c^2-d^2=0$ | the characteristic variety, equal to the zero divisor set | *Split-Quaternion Zero Divisors* |
| $x^{-1} = \bar{x}/N(x)$ | the inverse, singular on the null cone | *Split-Quaternion Algebra* |
| power series $\sum c_nx^n$ | convergence on a ball, evaluation entrywise | this article |
| $\mathrm{Cl}_{2,2}$ | the Clifford algebra of the full form, different from $\mathbb{H}_{\mathrm{s}}$ | *Clifford Algebras in Finite Dimensions* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the Dirac operator of an indefinite form and its hyperbolic character.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the elliptic theory against which the hyperbolic case is contrasted.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the failure of the identity theorem in an algebra with nilpotents.
- Vladimir I. Arnold, *Lectures on Partial Differential Equations* (Springer, 2004), for the wave operator, its characteristic cone and its lack of elliptic regularity.
