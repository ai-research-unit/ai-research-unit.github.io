
# __The Adjoint of the Left Multiplication on a Topological Vector Space__

## Introduction

A topological algebra $E$ over $\mathbb{K}$ with a continuous **trace** $\tau$ carries a canonical pairing of its own, the **trace form** $\langle x, y\rangle = \tau(xy)$, which needs no external form and no choice; it is continuous, symmetric and associative with respect to the multiplication, $\langle xy, z\rangle = \langle x, yz\rangle$, and it is the form of the category. With respect to it the left multiplication $L_{a}$ and the right multiplication $R_{a}$ are adjoint to one another, $(L_{a})^{\dagger} = R_{a}$ and $(R_{a})^{\dagger} = L_{a}$, which is the operator-level statement that the transposed multiplication is the multiplication on the other side. When the algebra also carries a continuous involution $\theta$ preserving the trace, the two operations mesh: $\theta$ is self-adjoint for the trace form, the induced operator involution $\theta L_{a}\theta$ has adjoint $\theta R_{\theta(a)}\theta$ when $\theta$ is an automorphism, and the trace-adjoint and the involution differ by the involution of the parameter.

This article develops the trace form and the adjoint of the left and the right multiplication on a topological algebra. The one-sided multiplications, their continuity and their composition laws are *The Left and Right Multiplication Operators on a Topological Vector Space*; the involution of the algebra and the transposed involution are *Locally Convex Spaces with an Involution* and *The Involution and the Dual Pairing*; the abstract adjoint defined by a dual pairing is *The Dual Pairing and the Adjoint*; the trace $\tau$ is a continuous linear functional with $\tau(xy) = \tau(yx)$. The signed version of the left multiplication is *The Signed Left Multiplication on a Topological Vector Space*, and its adjoint is *The Signed Adjoint of the Left Multiplication on a Topological Vector Space*. The forms are Part III.

Throughout, $E$ is a Hausdorff locally convex algebra over $\mathbb{K}$ with jointly continuous multiplication and a unit $1$, $\tau : E \to \mathbb{K}$ is a **continuous trace**, $\tau$ linear, continuous, with $\tau(xy) = \tau(yx)$, the **trace form** is $\langle x, y\rangle = \tau(xy)$ and is assumed non-degenerate, $L_{a}(x) = ax$ and $R_{a}(x) = xa$ are the left and the right multiplications, ${}^{\dagger}$ is the adjoint with respect to the trace form, and $\theta$ is a continuous algebra involution of $E$ preserving the trace, $\tau \circ \theta = \varsigma \circ \tau$.

## The Trace Form

**Definition.** The **trace form** of a topological algebra $E$ with a continuous trace $\tau$ is the continuous bilinear form

$$
\langle x, y\rangle = \tau(xy) \qquad (x, y \in E),
$$

with $\tau$ linear and continuous, $\tau(xy) = \tau(yx)$, and it is assumed **non-degenerate**: $\langle x, y\rangle = 0$ for all $y$ only when $x = 0$, and dually. The **trace-adjoint** of a continuous operator $S$ of $E$, when it exists, is the unique continuous $S^{\dagger}$ with $\langle Sx, y\rangle = \langle x, S^{\dagger}y\rangle$ for all $x, y$.

**Proposition (associativity and symmetry).** The trace form is symmetric, $\langle x, y\rangle = \langle y, x\rangle$, and associative with respect to the multiplication,

$$
\langle xy, z\rangle = \langle x, yz\rangle ,
$$

and the multiplications are adjoint families for it; the associativity is the compatibility of the form with the algebra structure, and it is the identity that all the adjoint computations of this group use.

**Proof.** Symmetry is $\tau(xy) = \tau(yx)$; associativity is $\langle xy,z\rangle = \tau(xyz) = \langle x, yz\rangle$, the middle factor moving through the trace by cyclicity; non-degeneracy makes the form a pairing, so that an adjoint is unique when it exists.

**Example (the standard instance).** On $E = \mathcal{L}(F)$ for a finite-dimensional $F$ the trace $\tau = \operatorname{tr}$ gives the trace form $\langle A, B\rangle = \operatorname{tr}(AB)$ of the corresponding article of the linear algebra; for a general topological algebra the trace is assumed and named, and the operators with a trace-adjoint are the ones continuous for the weak topology of the form.

## The Adjoint of the One-Sided Multiplications

**Theorem (the adjointness of the multiplications).** For every $a \in E$ the left and the right multiplication have adjoints with respect to the trace form, given by

$$
(L_{a})^{\dagger} = R_{a} , \qquad (R_{a})^{\dagger} = L_{a} .
$$

Consequently the adjoint of a left multiplication is a right multiplication, and conversely; the adjoint operation exchanges the two sides.

**Proof.** For $x, y \in E$, $\langle L_{a}x, y\rangle = \tau(axy) = \tau(xya) = \langle x, R_{a}y\rangle$, using the trace cyclicity; the uniqueness of the adjoint gives $(L_{a})^{\dagger} = R_{a}$. The second identity is the first with the multiplication reversed, or the direct computation $\langle R_{a}x, y\rangle = \tau(xay) = \tau(axy) = \langle x, L_{a}y\rangle$.

**Corollary (the adjoint of a two-sided sandwich).** For the unsigned sandwich $\Phi_{a,b}(x) = axb$ the adjoint is the sandwich with the parameters exchanged,

$$
(\Phi_{a,b})^{\dagger} = \Phi_{b,a} ,
$$

and the inner automorphism $\mathrm{Ad}_{a} = \Phi_{a,a^{-1}}$ has adjoint $\mathrm{Ad}_{a^{-1}}$, so the inner automorphisms are adjoint in the reverse order.

**Proof.** $\langle axb, y\rangle = \tau(axby) = \tau(xbya) = \langle x, bya\rangle = \langle x, \Phi_{b,a}y\rangle$, and $\mathrm{Ad}_{a^{-1}} = \Phi_{a^{-1},a} = \Phi_{a,a^{-1}}^{\dagger}$.

**Proposition (the algebra of adjointable operators).** The adjointable operators, those $S$ with an adjoint $S^{\dagger}$, form an algebra closed under the adjoint, and on them the adjoint reverses products, $(ST)^{\dagger} = T^{\dagger}S^{\dagger}$, is conjugate-linear and is its own inverse; the multiplications and the inner automorphisms are adjointable, so the algebra generated by them is an involutive algebra with respect to the trace form.

**Proof.** If $S$ and $T$ have adjoints then $\langle STx, y\rangle = \langle Tx, S^{\dagger}y\rangle = \langle x, T^{\dagger}S^{\dagger}y\rangle$, so $ST$ has adjoint $T^{\dagger}S^{\dagger}$; conjugate-linearity and the involution property are immediate from the definition and uniqueness, and the multiplications are adjointable by the theorem above.

## Compatibility with the Involution

**Theorem (the involution is self-adjoint for the trace form).** Let $\theta$ be a continuous algebra involution of $E$ preserving the trace, $\tau \circ \theta = \varsigma \circ \tau$. Then $\theta$ is metrically $\varsigma$-self-adjoint,

$$
\langle \theta x, y\rangle = \varsigma\bigl(\langle x, \theta y\rangle\bigr) \qquad (x, y \in E),
$$

so $\theta^{\dagger} = \theta$ up to the scalar involution, and $\theta$ is an isometry of the trace form, $\langle \theta x, \theta y\rangle = \varsigma(\langle x, y\rangle)$.

**Proof.** $\langle\theta x, y\rangle = \tau(\theta(x)y)$; applying $\tau\circ\theta = \varsigma\circ\tau$ and $\theta^{2} = \mathrm{id}$ and the trace cyclicity, $\tau(\theta(x)y) = \varsigma(\tau(\theta(\theta(x)y))) = \varsigma(\tau(x\theta(y))) = \varsigma(\langle x, \theta y\rangle)$. The isometry identity is the same computation with $y$ replaced by $\theta y$.

**Corollary (the induced operator involution).** For a continuous algebra involution $\theta$ preserving the trace and every $a \in E$,

$$
(\theta L_{a}\theta)^{\dagger} = \theta R_{a}\theta , \qquad (\theta R_{a}\theta)^{\dagger} = \theta L_{a}\theta ,
$$

so the conjugate of a left multiplication has adjoint the conjugate of the right multiplication of the same parameter. When $\theta$ is an automorphism this is $R_{\theta(a)}$ and $L_{\theta(a)}$; when $\theta$ is an anti-automorphism the two families are exchanged by conjugation, $\theta L_{a}\theta = R_{\theta(a)}$ and $\theta R_{a}\theta = L_{\theta(a)}$, and the formulas read $(\theta L_{a}\theta)^{\dagger} = L_{\theta(a)}$ and $(\theta R_{a}\theta)^{\dagger} = R_{\theta(a)}$.

**Proof.** Conjugating an adjointable operator by the self-adjoint isometry $\theta$ gives $(\theta S\theta)^{\dagger} = \theta S^{\dagger}\theta$; substituting $(L_{a})^{\dagger} = R_{a}$ gives the first formula and $(R_{a})^{\dagger} = L_{a}$ the second. If $\theta$ is an automorphism then $\theta R_{a}\theta = R_{\theta(a)}$ and $\theta L_{a}\theta = L_{\theta(a)}$; if it is an anti-automorphism then $\theta L_{a}\theta = R_{\theta(a)}$ and $\theta R_{a}\theta = L_{\theta(a)}$, whence the stated specialisations.

## Examples

**Example (the finite-dimensional instance).** For $E = \mathrm{End}_F(V)$ with $\tau = \operatorname{tr}$ the trace form is $\langle X,Y\rangle = \operatorname{tr}(XY)$ and the theorem gives $(L_{A})^{\dagger} = R_{A}$, $(R_{A})^{\dagger} = L_{A}$ and $(\Phi_{a,b})^{\dagger} = \Phi_{b,a}$; this is the computation of the corresponding article of the linear algebra, now with the operators read on a topological algebra and the adjoint continuous.

**Example (the trace-preserving conjugation).** On a Hilbert–Schmidt-type trace algebra the conjugation $\theta(x) = uxu^{-1}$ by a unitary $u$ is an algebra automorphism preserving the trace, and $\theta$ is self-adjoint for the trace form; the conjugate of $L_{a}$ has adjoint the conjugate of $R_{\theta(a)}$, so the adjoint commutes with the conjugation up to the exchange of sides.

**Example (the transposition involution).** On the algebra of matrices the transposition $\theta(A) = A^{\mathsf{T}}$ is an anti-automorphism preserving the trace, and it exchanges the left and the right multiplication, $\theta L_{A}\theta = R_{A^{\mathsf{T}}}$; the adjoint of the conjugate of $L_{A}$ is then the conjugate of $L_{\theta(A)}$, in agreement with the anti-automorphism case of the corollary.

## Summary

A topological algebra with a continuous trace $\tau$ carries the trace form $\langle x,y\rangle = \tau(xy)$, the form of the category: it is continuous, symmetric and associative, $\langle xy,z\rangle = \langle x,yz\rangle$, and non-degenerate by hypothesis. With respect to it the left and right multiplications are adjoint to one another, $(L_{a})^{\dagger} = R_{a}$ and $(R_{a})^{\dagger} = L_{a}$; the sandwich $\Phi_{a,b}$ has adjoint $\Phi_{b,a}$ and the inner automorphisms are adjoint in the reverse order; the adjointable operators form an involutive algebra on which ${}^{\dagger}$ reverses products. A continuous algebra involution $\theta$ preserving the trace is self-adjoint and isometric up to the scalar involution, $\langle\theta x,y\rangle = \varsigma(\langle x,\theta y\rangle)$, and this gives the compatibility of the trace-adjoint with the involution: $(\theta L_{a}\theta)^{\dagger} = \theta R_{\theta(a)}\theta$ when $\theta$ is an automorphism, the left and the right sides being exchanged when $\theta$ is an anti-automorphism. The finite-dimensional instance is the trace pairing $\operatorname{tr}(XY)$, and the conjugation and the transposition are the standard trace-preserving involutions. The signed versions are *The Signed Adjoint Sandwich on a Topological Vector Space* and *The Signed Adjoint of the Left Multiplication on a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $1$ | topological algebra with a unit |
| $\tau$ | continuous trace, $\tau(xy) = \tau(yx)$ |
| $\langle x,y\rangle = \tau(xy)$ | trace form, the form of the category |
| $L_{a}(x) = ax$, $R_{a}(x) = xa$ | left and right multiplication |
| ${}^{\dagger}$ | the trace-adjoint |
| $(L_{a})^{\dagger} = R_{a}$, $(R_{a})^{\dagger} = L_{a}$ | the adjointness |
| $(\Phi_{a,b})^{\dagger} = \Phi_{b,a}$ | the unsigned sandwich |
| $\theta$ | trace-preserving algebra involution, $\theta^{\dagger} = \theta$ |
| $(\theta L_{a}\theta)^{\dagger} = \theta R_{\theta(a)}\theta$ | the compatibility with the involution |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the traces, the Hilbert–Schmidt forms and the adjointable operators.
- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the traces and the trace forms on an operator algebra.
- Gottfried Köthe, *Topological Vector Spaces II* (Springer, 1979), for the topological algebras and their dual pairings.
- Albrecht Pietsch, *Operator Ideals* (North-Holland, 1980), for the trace functionals, the trace class and the duality of the ideal.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the topological algebras and the bilinear forms.
