# __Polarisation and the Hermitian Square__

## Introduction

A sesquilinear form is a function of two variables; its **diagonal** $q(x) = h(x,x)$ is a function of one. The diagonal determines the form only up to a well-defined part of it, and the passage from the diagonal back to the form is **polarisation**. The exact content of the passage, and the exact information the diagonal loses, are the subject of this article.

Two objects organise it. The **polarisation identity**

$$
q(x+y) - q(x) - q(y) = h(x,y) + h(y,x)
$$

recovers from the diagonal the **trace form** $h(x,y) + \varsigma(h(x,y))$, and leaves the skew-Hermitian part of $h$ unseen; at the trivial base involution and with $2$ invertible the passage is a bijection, and in characteristic two the diagonal sees nothing at all. And the **Hermitian square** $x^{*}x$ of the algebra is the element whose functional image is the diagonal, $q(x) = \varphi(x^{*}x)$, so that the quadratic form of the layer is carried by the involution of the algebra and not by the form alone.

This is the counterpart, in the sesquilinear layer, of *Quadratic Forms and Polarisation*, whose identity and whose characteristic-two degeneracy are the same. The form is *Sesqualgebras with a Form*, the matrix and quaternion quadratics are *Quadratic Forms over Algebras and Norms*, the trace form is *Hermitian Algebras*, and the real form that the trace form defines is *Real Forms and the Signature*. Throughout, $(A,*,h)$ is a sesqualgebra with a form over a base $(R,\varsigma)$, $\varphi = h(\cdot, 1)$ is the functional of the form, and $R^{\varsigma}$ is the fixed ring.

## The Diagonal

**Definition.** The **diagonal** of the form is the map

$$
q : A \longrightarrow R^{\varsigma}, \qquad q(x) = h(x,x) .
$$

It is valued in the fixed ring because $q(x) = \varsigma(q(x))$ is the Hermitian property read on the diagonal. The association $h \mapsto q$ is $R^{\varsigma}$-linear and it is the only part of the form that a single variable can see.

**Definition.** The **trace form** of $h$ is

$$
h_{\mathrm{tr}}(x,y) = h(x,y) + h(y,x) = h(x,y) + \varsigma(h(x,y)),
$$

the sum of the two orderings of the pair, and the **skew-Hermitian part** is $h_{\mathrm{sk}}(x,y) = h(x,y) - \varsigma(h(x,y))$. The two are the eigenspaces of the involution $h \mapsto h^{\dagger}$, $h^{\dagger}(x,y) = \varsigma(h(y,x))$, of *The Sesquilinear Form and the Conjugation*.

**Proposition.** The trace form is symmetric, $h_{\mathrm{tr}}(x,y) = h_{\mathrm{tr}}(y,x)$, and $R^{\varsigma}$-bilinear; the skew-Hermitian part is alternating, $h_{\mathrm{sk}}(x,x) = 0$. Every form is the sum $h = \tfrac{1}{2}h_{\mathrm{tr}} + \tfrac{1}{2}h_{\mathrm{sk}}$ when $2$ is invertible in $R^{\varsigma}$.

**Proof.** Symmetry and bilinearity are immediate from the definition and from $R^{\varsigma} = R^{\varsigma\cdot\varsigma}$. For the alternating property, $h_{\mathrm{sk}}(x,x) = h(x,x) - \varsigma(h(x,x)) = 0$ because the diagonal lies in $R^{\varsigma}$. The decomposition is the eigenvector decomposition of the involution $h \mapsto h^{\dagger}$ of the space of the sesquilinear forms, which needs $\tfrac{1}{2}$.

Note that $h_{\mathrm{tr}}$ is not $R$-sesquilinear when $\varsigma \neq \mathrm{id}$: it carries $\lambda$ to $\tfrac{1}{2}(\lambda + \varsigma(\lambda))$-weight, so it is a form over the fixed ring and not over $R$. This is why the two classical readings over $\mathbb{R}$ and over $\mathbb{C}$ differ, and the difference is worked in the examples below.

## Polarisation

**Proposition (the polarisation identity).** For all $x, y \in A$,

$$
q(x+y) = q(x) + q(y) + h_{\mathrm{tr}}(x,y) .
$$

**Proof.** Expand by biadditivity: $q(x+y) = h(x,x) + h(x,y) + h(y,x) + h(y,y) = q(x) + q(y) + h(x,y) + h(y,x)$, and the last two terms are $h_{\mathrm{tr}}(x,y)$.

**Corollary (the diagonal recovers the trace form).** If $2$ is invertible in $R^{\varsigma}$ then

$$
h_{\mathrm{tr}}(x,y) = q(x+y) - q(x) - q(y),
$$

so two forms with the same diagonal have the same trace form and differ by a skew-Hermitian form.

**Corollary (the classical case).** When $\varsigma = \mathrm{id}$ and $2$ is invertible, the polarisation $h(x,y) = \tfrac{1}{2}\bigl(q(x+y) - q(x) - q(y)\bigr)$ is a bijection between the symmetric bilinear forms and the quadratic functions $q$ with $q(\lambda x) = \lambda^{2}q(x)$. This is the correspondence of *Quadratic Forms and Polarisation*, and the sesquilinear layer is its $\varsigma$-twisted version.

**Remark (what the diagonal does not see).** The skew-Hermitian part is invisible to the diagonal: $h$ and $h - h_{\mathrm{sk}}$ have the same diagonal, and $h_{\mathrm{sk}}(x,x) = 0$ for every $x$. Over $\mathbb{C}$ with $\varsigma$ the conjugation, the trace form $\tfrac{1}{2}h_{\mathrm{tr}} = \operatorname{Re} h$ is a real symmetric form and the skew part $\tfrac{1}{2}h_{\mathrm{sk}} = \mathrm{i}\,\operatorname{Im} h$ is real alternating; a Hermitian form is exactly a real symmetric form together with a real alternating form tied by the complex structure, and this is the decomposition $h = g + \mathrm{i}\,\omega$ of the geometry of a Kähler manifold.

## The Hermitian Square

The diagonal of the layer is computed by the algebra, because the functional of the form is evaluated on the Hermitian square.

**Proposition.** The diagonal is the functional image of the **Hermitian square**:

$$
q(x) = \varphi(x^{*}x), \qquad \varphi = h(\cdot, 1),
$$

and $x^{*}x$ is self-adjoint, $(x^{*}x)^{*} = x^{*}x$.

**Proof.** $\varphi(x^{*}x) = h(x^{*}x, 1) = h(x, x^{*}1) = h(x,x)$, by the compatibility $h(ab,c) = h(b,a^{*}c)$ read at $(a,b,c) = (x^{*},x,1)$ and by $1^{*} = 1$. Self-adjointness is the involution axiom, $(x^{*}x)^{*} = x^{*}x^{**} = x^{*}x$.

**Corollary.** The **quadratic form of the algebra** $Q(x) = \varphi(x^{*}x)$ satisfies $Q(x) = h(x,x)$, and its polarisation is the trace form, $Q(x+y) - Q(x) - Q(y) = h_{\mathrm{tr}}(x,y)$.

The two products $x^{*}x$ and $xx^{*}$ are the two Hermitian squares of the element, exchanged by the involution. The second gives the same diagonal for a **cyclic** functional, in particular for the trace form $\varphi = \tau$, where $\varphi(xx^{*}) = \varphi(x^{*}x)$ and the diagonal is also the functional image of $xx^{*}$; for a non-cyclic functional the two differ, and it is $x^{*}x$ that the diagonal reads. The square is the **norm map** of the layer; it is quadratic over $R^{\varsigma}$ in the sense $(\lambda x)^{*}(\lambda x) = \varsigma(\lambda)\lambda\,x^{*}x = |\lambda|^{2}x^{*}x$, and it is multiplicative for the elements of the unitary slice, $(xy)^{*}(xy) = y^{*}(x^{*}x)y$. When the norm map is multiplicative on the whole algebra the form is that of a composition algebra, and the norm form of the quaternion and octonion algebras is the classical instance: the polarisation of the norm is the trace form, and the whole theory is *Hermitian Forms over Algebras and Norms*.

## The Failure When 2 Is Not Invertible

**Proposition.** In characteristic two with $\varsigma = \mathrm{id}$ the polarisation identity degenerates: $q(x+y) = q(x) + q(y)$, the trace form vanishes, and the diagonal determines no part of the form at all.

**Proof.** With $\varsigma = \mathrm{id}$ the form is symmetric, $h_{\mathrm{tr}} = 2h = 0$, and the polarisation identity reduces to additivity of $q$. A symmetric bilinear form and its diagonal are then unrelated data: an alternating form has a vanishing diagonal and is not zero, and distinct symmetric forms share the diagonal.

The quadratic datum is therefore strictly finer than the bilinear one when $2$ is not invertible: a **quadratic refinement** of the form is a function $q$ with $q(x+y) - q(x) - q(y) = h(x,y)$, and it is an extra structure. The characteristic-two examples, including the Hermitian-and-skew-Hermitian-not-alternating form over $\mathbb{F}_{2}$, are worked in *The Sesquilinear Form and the Conjugation*; the quadratic forms themselves are *Quadratic Forms and Polarisation*.

## Examples

### The Matrices

On $M_n(\mathbb{C})$ with $h(X,Y) = \tau(XY^{*})$ the diagonal is $q(X) = \tau(XX^{*}) = \sum_{ij}|X_{ij}|^{2}$, the square of the Frobenius norm, and the polarisation recovers $\tau(XY^{*} + YX^{*}) = 2\operatorname{Re}\tau(XY^{*})$. The form is Hermitian, its trace form is the real symmetric form of the real and imaginary parts of the trace pairing, and its skew part is the alternating form $\mathrm{i}\operatorname{Im}\tau(XY^{*})$.

### The Real and the Complex Reading

Over $\mathbb{R}$ with the trivial involution every Hermitian form is symmetric and the polarisation is a bijection when $2$ is invertible. Over $\mathbb{C}$ it is not: the diagonal of a Hermitian form sees $\operatorname{Re}h$ and never $\operatorname{Im}h$, and the pair $(\operatorname{Re}h, \operatorname{Im}h)$ is the pair (symmetric, alternating) of the real reading. The transfer between the two readings is *Real Forms and the Signature*.

### The Biquaternion Form

On $\mathbb{B}$ with the dagger, $q(\tilde Q) = \operatorname{Sc}(\tilde Q\tilde Q^{\dagger}) = \sum_{\mu}|Q_{\mu}|^{2}$, and the polarisation gives the real symmetric form $\operatorname{Re}\operatorname{Sc}(\tilde P\tilde Q^{\dagger})$ together with the alternating form $\operatorname{Im}\operatorname{Sc}(\tilde P\tilde Q^{\dagger})$. The indefinite companion $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$ and its signature are *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## Summary

- The **diagonal** $q(x) = h(x,x)$ is valued in the fixed ring $R^{\varsigma}$ and is the only part of the form visible to one variable.
- The **polarisation identity** reads $q(x+y) - q(x) - q(y) = h_{\mathrm{tr}}(x,y)$, the trace form.
- The trace form is symmetric and $R^{\varsigma}$-bilinear, the skew-Hermitian part $h_{\mathrm{sk}}$ is alternating, and $h = \tfrac{1}{2}h_{\mathrm{tr}} + \tfrac{1}{2}h_{\mathrm{sk}}$ when $2$ is invertible: the diagonal recovers the trace form and never the skew part.
- Over $\mathbb{C}$ the decomposition is $\operatorname{Re}h + \mathrm{i}\operatorname{Im}h$, a real symmetric form and a real alternating form.
- The diagonal is the functional image of the **Hermitian square**, $q(x) = \varphi(x^{*}x)$, and the quadratic form $Q(x) = \varphi(x^{*}x)$ has the trace form for its polarisation; for a cyclic functional the square $xx^{*}$ gives the same diagonal.
- In characteristic two with the trivial involution the polarisation degenerates, the diagonal determines nothing, and a quadratic refinement is extra structure.
- The classical bilinear original is *Quadratic Forms and Polarisation*; the norm forms of the algebras are *Hermitian Forms over Algebras and Norms*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $q$ | the diagonal $h(x,x)$ of the form |
| $h_{\mathrm{tr}}$ | the trace form $h(x,y) + \varsigma(h(x,y))$ |
| $h_{\mathrm{sk}}$ | the skew-Hermitian part $h(x,y) - \varsigma(h(x,y))$ |
| $h^{\dagger}$ | the involution $h^{\dagger}(x,y) = \varsigma(h(y,x))$ on the forms |
| $\varphi$ | the functional $h(\cdot,1)$ |
| $xx^{*}$ | the Hermitian square of $x$ |
| $Q(x) = \varphi(xx^{*})$ | the quadratic form of the algebra |
| $R^{\varsigma}$ | the fixed ring of the base involution |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the polarisation of a form, the trace form and the characteristic-two degeneration.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the quadratic refinements and the failure of polarisation in characteristic two.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the trace form of a Hermitian form over a ring with an involution.
