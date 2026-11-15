# __The Two Forms and the Two Algebraic Norms of the Complex Space__

## Introduction

A form on an algebra is the scalar part of a product, with a conjugation named on each slot. The complex space carries two products, so it carries two forms, and each form read at its two equal arguments is an algebraic norm. The forms are $P(Q_1,Q_2)=Q_1Q_2$, the plain form, and $H(Q_1,Q_2)=Q_1\bar Q_2$, the Hermitian form. The norms are $P(Q)=Q^{2}$ and $H(Q)=Q\bar Q$.

The two are as different as two forms on one space can be. The plain form is symmetric, complex-valued, of realified signature $(1,1)$, isotropic, with no positive cone and no order; its norm is complex, anisotropic and not real. The Hermitian form is conjugate-symmetric, positive definite, of realified signature $(2,0)$, multiplicative; its norm is the squared modulus. One function, $H$, is at once a form, a norm and a square of the algebra.

The two products are *The Two Products of the Complex Space*, and the general convention of a form is *Product and Form Conventions*; the norm of the definite form, its multiplicativity, the invertibility criterion and the group of units are *Complex Norm and Invertibility*. The positivity and the cone are *The Positivity and the Ray of Squares of the Complex Space*, and the Hermitian modules over the algebra are *The Hermitian Modules and the Unitary Witt Group over the Complex Algebra*.

**Interpretation.** The elements are $Q_1=q_1+iq'_1$ and $Q_2=q_2+iq'_2$, with real coordinates. A form is written with two arguments and a norm with one, and the brackets $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ name the four forms of the general theory. A bracket is reserved for a form and is never an element. The letters of the forms are $P$ and $H$; the letter $B$ is not used for a form here, the corpus keeping it for the complex modulus of a vector part and for a right annihilator.

## The Four Forms and the Two That Survive

The general theory reads a form by the two conjugations its product carries, and the table lists the four and their images.

| the general form | its product | its image on $\mathbb{C}$ | its norm |
|---|---|---|---|
| $\langle\cdot,\cdot\rangle$ | $Q_1Q_2$ | $P(Q_1,Q_2)=Q_1Q_2$ | $P(Q)=Q^{2}$ |
| $\langle\cdot,\cdot\rangle_{\natural}$ | $Q_1^{\natural}Q_2$ | $P(Q_1,Q_2)=Q_1Q_2$ | $N(Q)=Q^{2}$ |
| $\langle\cdot,\cdot\rangle_{*}$ | $Q_1Q_2^{*}$ | $H(Q_1,Q_2)=Q_1\bar Q_2$ | $H(Q)=Q\bar Q$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$ | $Q_1^{\natural}Q_2^{*}$ | $H(Q_1,Q_2)=Q_1\bar Q_2$ | $\mathrm{Kr}(Q)=Q\bar Q$ |

**Proposition.** The four forms fall two-and-two onto two, and the two identities $N=P$ and $\mathrm{Kr}=H$ hold.

*Proof.* The intrinsic conjugation ${}^{\natural}$ is the identity on $\mathbb{C}$, so the second and the fourth rows coincide with the first and the third.

**Remark (the general letter survives without an object).** The letters $N$ and $\mathrm{Kr}$ keep their place in the corpus's list of four, and on $\mathbb{C}$ they name the two forms of the plain and Hermitian kinds. A reader who sees $N$ in a general article must not read it as a complex norm: the coincidence is a coincidence of the complex layer, and it is recorded here once so that it is not read as an identity in general.

## The Plain Form

**Definition.** The **plain form** is $P(Q_1,Q_2)=Q_1Q_2$, the multiplication of the field.

**Proposition.** The plain form is $\mathbb{C}$-bilinear, symmetric and non-degenerate.

*Proof.* Bilinearity is the distributivity of the field in each variable and the associativity of the scalars; symmetry is the commutativity of the multiplication. Non-degeneracy: if $P(Q_1,Q_2)=0$ for all $Q_2$, then $Q_1=0$ by the choice $Q_2=1$, and the field has no zero divisor.

### The Gram Matrix

Over $\mathbb{C}$ the space is one-dimensional with the basis $(1)$, and the Gram matrix is the one-by-one matrix with the single entry $P(1,1)=1$.

### The Realified Signature

**Proposition.** The realified symmetric bilinear form $\operatorname{Re}P$ has the Gram matrix $\mathrm{diag}(1,-1)$ on the real basis $(1,i)$ and the signature $(1,1)$.

*Proof.* $\operatorname{Re}P(1,1)=1$, $\operatorname{Re}P(1,i)=0$, $\operatorname{Re}P(i,i)=-1$.

### The Null Lines

**Proposition.** The realified form is isotropic: $\operatorname{Re}P(Q,Q)=0$ for the two non-zero elements $Q=1+i$ and $Q=1-i$.

*Proof.* $(1\pm i)^{2}=\pm2i$, whose real part is zero.

The null cone of $\operatorname{Re}P$ is therefore the pair of real lines spanned by $1+i$ and $1-i$, that is, the two diagonals of the real plane.

**Remark (the two readings of isotropy).** The complex-valued form $Q_1Q_2$ has no non-zero isotropic vector, because $Q^{2}=0$ forces $Q=0$ in a field. The realified form does have them. The two statements do not conflict: isotropy is a property of a real form, and the complex form is not a real form. The word *isotropic* is therefore read on the realification throughout this article.

**Remark (no positive cone, no order).** The plain form takes complex values and its real part is indefinite, so there is no set of positive elements for it and no order attached to it. The signature $(1,1)$ says exactly why: the set where $\operatorname{Re}P$ is non-negative is a double cone of two opposite components, not a positive cone, and a double cone with two components defines no order. The Hermitian form is the one that carries positivity, and the only order of the complex field is the order inherited from its real part, which is not compatible with the multiplication, as *The Specificities of the Complex Algebra* shows.

## The Hermitian Form

**Definition.** The **Hermitian form** is $H(Q_1,Q_2)=Q_1\bar Q_2$.

**Proposition.** The Hermitian form is conjugate-symmetric, $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, and positive definite: $H(Q,Q)\ge0$ with equality only at $Q=0$.

*Proof.* Conjugate symmetry: $\overline{H(Q_2,Q_1)}=\overline{Q_2\bar Q_1}=Q_1\bar Q_2$. The slot rules are the slot rules of the sesquilinear product. Definiteness: $Q\bar Q=q^{2}+(q')^{2}$, a sum of two real squares.

**Proposition.** The realified form $\operatorname{Re}H$ has the Gram matrix $I_2$ on the real basis $(1,i)$ and the signature $(2,0)$.

*Proof.* $\operatorname{Re}H(1,1)=1$, $\operatorname{Re}H(1,i)=0$, $\operatorname{Re}H(i,i)=1$.

**Proposition.** The Hermitian form is multiplicative: $H(Q_1Q_2)=H(Q_1)H(Q_2)$.

*Proof.* $H(Q_1Q_2)=Q_1Q_2\overline{Q_1Q_2}=Q_1\bar Q_1Q_2\bar Q_2$, the modulus being multiplicative.

**Remark (both Gram matrices over $\mathbb{C}$).** Over $\mathbb{C}$ both forms have the Gram matrix $[1]$: the plain form because $P(1,1)=1$ and the Hermitian form because $H(1,1)=1$. The two forms are separated by their symmetry and not by their matrix, and that is exactly the point: over $\mathbb{C}$ a symmetric form and a conjugate-symmetric form can have the same Gram matrix and behave in opposite ways on the realification.

## The Two Algebraic Norms

### The Plain Norm

**Definition.** The **plain norm** is $P(Q)=P(Q,Q)=Q^{2}$.

**Proposition.** The plain norm is complex-valued, multiplicative and anisotropic: $P(Q_1Q_2)=P(Q_1)P(Q_2)$, and $P(Q)=0$ only at $Q=0$.

*Proof.* The multiplicativity is $(Q_1Q_2)^{2}=Q_1^{2}Q_2^{2}$; the anisotropy is the absence of a zero divisor.

The plain norm takes every non-zero complex value exactly twice, at $Q$ and at $-Q$, and it is neither real, nor non-negative, nor definite.

### The Hermitian Norm

**Definition.** The **Hermitian norm** is $H(Q)=H(Q,Q)=Q\bar Q=q^{2}+(q')^{2}$.

**Proposition.** The Hermitian norm is real, non-negative, definite and multiplicative, and it is the square of the modulus.

*Proof.* The reality and the value are the coordinates; the definiteness is the proposition of §*The Hermitian Form*; the multiplicativity is the multiplicativity of $H$ read at the two equal arguments.

### The Two Norms Compared

| the property | $P(Q)=Q^{2}$ | $H(Q)=Q\bar Q$ |
|---|---|---|
| the value | complex | real, non-negative |
| definite | no | yes |
| multiplicative | yes | yes |
| the zero set | $\{0\}$ | $\{0\}$ |
| the range | $\mathbb{C}$ | $[0,\infty)$ |
| the level set of $1$ | the two points $\pm1$ | the unit circle |

**Remark (the precise sense of *the only one*).** Both norms are multiplicative, and both vanish only at the origin. Only the Hermitian norm is real and definite, and that is the sense in which it is the norm of the algebra: it is the one that measures, the other one multiplying values without measuring anything.

## The Two Forms on the Two Lines

### The Real Line

**Proposition.** On the real line the two forms coincide: $P(q_1,q_2)=H(q_1,q_2)=q_1q_2$ for real $q_1,q_2$.

*Proof.* The conjugate of a real number is itself.

On the real line both forms are positive definite, and both norms are the square of the real coordinate.

### The Imaginary Line

**Proposition.** On the imaginary line the two forms are opposite: $P(iq'_1,iq'_2)=-q'_1q'_2=-H(iq'_1,iq'_2)$.

*Proof.* $(iq'_1)(iq'_2)=-q'_1q'_2$, and $(iq'_1)\overline{(iq'_2)}=q'_1q'_2$.

**Theorem.** The restriction of $\operatorname{Re}P$ to the real line is positive definite and its restriction to the imaginary line is negative definite; the restriction of $\operatorname{Re}H$ is positive definite on both. Hence the signature $(1,1)$ of the plain form and the signature $(2,0)$ of the Hermitian form.

*Proof.* The two lines are orthogonal for both realified forms, and the values on a line are those of the propositions above. A form whose restrictions to two orthogonal lines are of signs $(+,-)$ has signature $(1,1)$, and one whose restrictions are $(+,+)$ has signature $(2,0)$.

**Remark (the count of signs).** The whole difference between the two forms is the sign on the imaginary line. The plain form multiplies two imaginary numbers into a negative real, and the Hermitian form conjugates one of them first and so multiplies two into a positive. Every statement of this article is a consequence of that one sign.

## The One Function That Is a Form, a Norm and a Square

**Remark (the triple identity of $H$).** The function $H$ is three things at once. With two arguments it is the Hermitian form; with two equal arguments it is the algebraic norm; and its value at two equal arguments is the square of the algebra, $Q\bar Q$, which is also the Hermitian square of *The Classes of Element of the Complex Algebra*. No other function of the complex space has the three readings. The plain form is a form and it has a diagonal, but the diagonal is complex and indefinite, so it measures nothing; the modulus $|Q|$ measures, but it is a square root rather than a square.

**Proposition (the polarisation of the plain norm).** The plain norm polarises in two terms:

$$
P(Q_1,Q_2)=\tfrac12\bigl[P(Q_1+Q_2)-P(Q_1)-P(Q_2)\bigr].
$$

*Proof.* Expand $(Q_1+Q_2)^{2}=Q_1^{2}+2Q_1Q_2+Q_2^{2}$.

**Proposition (the polarisation of the Hermitian norm).** The Hermitian norm polarises in four terms:

$$
H(Q_1,Q_2)=\tfrac12\bigl[H(Q_1+Q_2)-H(Q_1)-H(Q_2)\bigr]+\tfrac{i}{2}\bigl[H(Q_1+iQ_2)-H(Q_1)-H(Q_2)\bigr].
$$

*Proof.* $H(Q_1+Q_2)=H(Q_1)+H(Q_2)+2\operatorname{Re}H(Q_1,Q_2)$ and $H(Q_1+iQ_2)=H(Q_1)+H(Q_2)+2\operatorname{Im}H(Q_1,Q_2)$, so the two brackets are $2\operatorname{Re}H(Q_1,Q_2)$ and $2\operatorname{Im}H(Q_1,Q_2)$.

**Remark (why two terms and four).** A square polarises in two terms exactly when the form is bilinear, and in four when it is sesquilinear. The plain norm is the square of a bilinear form and the Hermitian norm is the square of a sesquilinear one, and the arity of the polarisation is the arity of the form. This is the same distinction as the one between the two products, read on the diagonal.

## Summary

The complex space carries two forms, $P(Q_1,Q_2)=Q_1Q_2$ and $H(Q_1,Q_2)=Q_1\bar Q_2$, because the intrinsic conjugation is the identity and the four forms of the general theory fall two-and-two, with $N=P$ and $\mathrm{Kr}=H$. The plain form is symmetric, non-degenerate, of realified signature $(1,1)$, isotropic on the two null lines $q=\pm q'$, with no positive cone and no order; its norm $Q^{2}$ is complex, anisotropic and multiplicative. The Hermitian form is conjugate-symmetric, positive definite, of realified signature $(2,0)$, multiplicative; its norm $Q\bar Q$ is real, non-negative and definite, and it polarises in four terms where the plain norm polarises in two. On the real line the two forms coincide, on the imaginary line they are opposite, and the whole difference between the two signatures is the sign of the square of an imaginary number. One function, $H$, is at once a form, a norm and a square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P(Q_1,Q_2)=Q_1Q_2$ | the plain form, also $N$; the plain norm is $P(Q)=Q^{2}$ |
| $H(Q_1,Q_2)=Q_1\bar Q_2$ | the Hermitian form, also $\mathrm{Kr}$; the norm is $H(Q)=Q\bar Q$ |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$ | the two bilinear brackets, both equal to $P$ |
| $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the two sesquilinear brackets, both equal to $H$ |
| $\operatorname{Re}P$, $\operatorname{Re}H$ | the realified forms, of signatures $(1,1)$ and $(2,0)$ |
| $1\pm i$ | the two isotropic elements of the realified plain form |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for symmetric and Hermitian forms over an algebra with involution, their signatures and their classification.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for symmetric bilinear forms, isotropy, the Witt decomposition and the signature of a real form.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, second edition, 1974), for sesquilinear forms, their Gram matrices and the polarisation identities.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the trace form and the norm form of an algebra and their behaviour under the realification.
