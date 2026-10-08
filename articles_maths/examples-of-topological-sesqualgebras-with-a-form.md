# __Examples of Topological Sesqualgebras with a Form__

## Introduction

The layer with a form has two definitions, the topological object with a continuous compatible Hermitian form and the normed or complete object in which the form is definite and its diagonal is a submultiplicative norm of *The Norm Defined by a Form*, and the examples are what separate them. The examples below are the sesqualgebras of *Examples of Topological Sesqualgebras* — associative algebras with an involution, read through the derived product $x \star y = xy^{*}$ — each with a Hermitian form $h$ compatible with the product, $h(xy,z) = h(y,x^{*}z)$, and the ring of dual numbers $\mathbb{C}[t]/(t^{2})$ is adjoined as the smallest algebra carrying an indefinite compatible form; what distinguishes them is whether the form is **definite** or **indefinite**, whether it is **compatible** or merely Hermitian, whether the norm it defines is **submultiplicative** and whether it satisfies the $\mathrm{C}^{*}$-condition, and whether the object is **complete**. The four standard models are definite and compatible and differ in the last three; the biquaternion algebra carries two forms, one definite and compatible and one indefinite and **not** compatible, so definiteness and compatibility are independent; the dual numbers carry two forms, one indefinite and compatible and one semi-definite with a nonzero radical, so definiteness is a genuine restriction; and the degenerate zero form is the witness that nondegeneracy is a hypothesis and not a consequence.

Three facts organise the article. The **four standard models** — the field, the matrices with the trace form, the group algebra with the $L^{2}$ form, and the function algebra with the $L^{2}$ form — are the definite and compatible examples of the layer, and they separate the properties that the definitions do not: the field is complete with a submultiplicative norm satisfying the $\mathrm{C}^{*}$-condition, the matrices are complete with a submultiplicative norm that fails the $\mathrm{C}^{*}$-condition, the group algebra is complete with a norm that is not submultiplicative at all, and the function algebra is not even complete, its norm being neither submultiplicative nor complete. The **indefinite examples** show that an indefinite Hermitian form on an algebra can be compatible — the dual numbers with $h(a+bt,c+dt) = a\overline{d}+b\overline{c}$, of signature $(1,1)$ — or not, the biquaternion quaternion sesquilinear form $h_{\natural*}$ of signature $(2,6)$ being the standard witness, and the second supplies the input of *The Fundamental Symmetry of the Form* while the first is the caution that indefiniteness and compatibility are separate hypotheses. And the **semi-definite and degenerate** examples, the form $h_{0}(a+bt,c+dt) = a\overline{c}$ with the radical $tA$ and the zero form with radical $A$, are the witnesses that the radical of a form of the layer can be a proper ideal and that the definiteness of the normed object is exactly the vanishing of the radical, the statement of the completion theorems of *The Completion of a Sesqualgebra with a Form*.

The article presents the four standard models, the indefinite models and the degenerate ones, tabulates the invariants of each, and records the collapse. The layer without a form is *Examples of Topological Sesqualgebras*; the norm and its axioms are *The Norm Defined by a Form*; the compatibility and the radical are *Topological Sesqualgebras with a Form*; the biquaternion pairings are *The Four Pairings of the Biquaternion Algebra* and *The Biquaternion Krein Form and Its Signature*. Throughout, $A$ is a topological sesqualgebra over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$, $*$ its continuous $\varsigma$-semilinear involution, $h$ a continuous Hermitian form, linear in the first slot and $\varsigma$-semilinear in the second, and the derived product is $x \star y = xy^{*}$.

## The Four Standard Models

### The Field

**Example (the field, verdict: complete, submultiplicative, $\mathrm{C}^{*}$).** Let $A = \mathbb{C}$ with its product, $* = \varsigma$ the conjugation and $h(z,w) = z\overline{w}$, the form of *The Norm Defined by a Form*, §*The Field*. The form is Hermitian, compatible, positive definite and nondegenerate, of signature $(2,0)$ over $\mathbb{R}$; the norm is the modulus, $\lVert z\rVert = \lvert z\rvert$; Cauchy–Schwarz is an equality for every pair because a one-dimensional space has proportional vectors; the norm is submultiplicative, $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$, and satisfies the $\mathrm{C}^{*}$-condition, $\lvert z^{*}z\rvert = \lvert z\rvert^{2}$. The radical is zero, the derived product is $z\star w = z\overline{w}$, of norm one, and the object is the smallest of the layer in which every property holds.

### The Matrices

**Example (the matrices, verdict: complete, submultiplicative, no $\mathrm{C}^{*}$).** Let $A = M_{n}(\mathbb{C})$ with the conjugate transpose and the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$, the model of the layer. The form is Hermitian, compatible, positive definite, nondegenerate and of signature $(2n^{2},0)$ over $\mathbb{R}$; the norm is the **Frobenius norm**, the Euclidean norm of the $n^{2}$ entries, submultiplicative by Cauchy–Schwarz on the entries and with $\lVert E_{ij}\rVert = 1$ on the matrix units. The norm is **not** the $\mathrm{C}^{*}$-norm: $\lVert 1\rVert^{2} = n$ while $\lVert 1^{*}1\rVert = \sqrt{n}$, so the $\mathrm{C}^{*}$-condition fails for $n \geq 2$, and correspondingly the operator norm of $m_{1}$ is $1$ while $\lVert 1\rVert = \sqrt{n}$. The radical is zero, the involution is isometric, and the example is the model of the article and the first witness that the $\mathrm{C}^{*}$-condition is a restriction on the object and not a consequence of definiteness.

### The Group Algebra

**Example (the group algebra, verdict: complete, not submultiplicative).** Let $G$ be a finite group, let $A = \mathbb{C}[G]$ with the convolution product, the involution $f^{*}(x) = \overline{f(x^{-1})}$ and the $L^{2}$ form

$$
h(f,g) = \sum_{x\in G} f(x)\overline{g(x)} ,
$$

the form of the Hilbert algebra of *Hilbert Algebras*. The form is Hermitian, compatible and positive definite, of signature $(2\lvert G\rvert,0)$ over $\mathbb{R}$, and the object is complete because it is finite dimensional; but the norm is **not submultiplicative**: at the constant function $\mathbf{1}$ one has $(\mathbf{1}*\mathbf{1})(x) = \lvert G\rvert$, so $\lVert\mathbf{1}*\mathbf{1}\rVert = \lvert G\rvert^{3/2}$ while $\lVert\mathbf{1}\rVert^{2} = \lvert G\rvert$, which is smaller as soon as $\lvert G\rvert \geq 2$. The example is therefore a *topological* sesqualgebra with a form that is **not normed by its form**: it satisfies every hypothesis of the layer except the submultiplicativity of *The Norm Defined by a Form*, §*The Submultiplicative Norm*, and it is the witness that the submultiplicativity must be assumed. Its derived product is $f\star g = f*g^{*}$, of norm $\lvert G\rvert^{1/2}$.

### The Function Algebra

**Example (the function algebra, verdict: incomplete and not submultiplicative).** Let $X$ be a compact space with a finite measure $\mu$ of full support, let $A = C(X,\mathbb{C})$ with the pointwise product, the involution $f^{*} = \overline{f}$ and the $L^{2}$ form

$$
h(f,g) = \int_{X} f\,\overline{g}\,d\mu .
$$

The form is Hermitian, compatible and positive definite, of infinite signature over $\mathbb{R}$, and the object is **not complete** in the norm it defines, which is the $L^{2}$ norm: the completion is the Hilbert space $L^{2}(X,\mu)$, in which the algebra is dense but in which the product does not extend, since the product of two $L^{2}$ functions need not be in $L^{2}$. The norm is also **not submultiplicative**: for the indicator $f$ of a half of a space of measure $1$ one has $\lVert f^{2}\rVert = 2^{-1/2}$ while $\lVert f\rVert^{2} = 2^{-1}$, so the inequality fails. The example is the witness that neither completeness nor submultiplicativity follows from definiteness, and it is the boundary of *The Completion of a Sesqualgebra with a Form*: the completion exists as a Hilbert space, but the object of the layer is not recovered on it.

## The Indefinite and the Semi-Definite Models

### The Biquaternion Algebra

**Example (the biquaternion algebra, the two sesquilinear forms).** On the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the Hermitian conjugation $*$, the **complex sesquilinear form**

$$
h_{*}(P,Q) = \operatorname{Sc}(PQ^{*}) = \sum_{\mu} P_{\mu}\overline{Q_{\mu}}
$$

is Hermitian, compatible, positive definite, nondegenerate and of signature $(8,0)$ over $\mathbb{R}$, and its norm is the Euclidean norm of the eight real coordinates, the one of *The Euclidean Topology of the Biquaternion Algebra*; it is the definite model of *The Norm Defined by a Form*, §*The Biquaternion Trace Form*, and neither submultiplicativity nor the $\mathrm{C}^{*}$-condition holds for it: at the zero divisor $P = Q = 1 + \mathrm{i}e_{1}$, with $\mathrm{i} \in \mathbb{C}$ the scalar and $e_{1}$ the quaternion unit, one has $\lVert PQ^{*}\rVert = 2\sqrt{2}$ against $\lVert P\rVert\lVert Q\rVert = 2$ and $\lVert P^{*}P\rVert = 2\sqrt{2}$ against $\lVert P\rVert^{2} = 2$, while at the unit both hold, $\lVert 1\rVert^{2} = \lVert 1^{*}1\rVert = 1$. The **quaternion sesquilinear form**

$$
h_{\natural*}(P,Q) = \operatorname{Sc}(P^{\natural}Q^{*}) = \sum_{\mu}\varepsilon_{\mu}P_{\mu}\overline{Q_{\mu}} , \qquad \varepsilon = (1,-1,-1,-1) ,
$$

is Hermitian, nondegenerate and **indefinite**, of signature $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$; it is **not compatible** with the product, and the witness is the element $e_{1}$: with $P = Q = e_{1}$ and $R = 1$ one has $h_{\natural*}(PQ,R) = -1$ while $h_{\natural*}(Q,P^{*}R) = 1$, so the identity of the compatibility fails. The pair of forms is the finite-dimensional witness that definiteness and compatibility are independent conditions on a Hermitian form, and the second is the input of the indefinite theory of *The Fundamental Symmetry of the Form* and *The Biquaternion Krein Form and Its Signature*, whose isometry group is $U(1,3)$.

### The Dual Numbers

**Example (the dual numbers, an indefinite compatible form).** Let $A = \mathbb{C}[t]/(t^{2})$ with the involution $*$ acting by the conjugation on the coefficients and fixing $t$, so that $(a+bt)^{*} = \overline{a}+\overline{b}t$; the algebra is the ring of dual numbers over $\mathbb{C}$, a local algebra in which $t$ is a nilpotent of square zero. For real $\alpha,\beta$ with $\beta \neq 0$, put

$$
h(a+bt, c+dt) = \alpha\, a\overline{c} + \beta\bigl(a\overline{d}+b\overline{c}\bigr) .
$$

Then $h$ is Hermitian, nondegenerate, of Gram matrix $\begin{pmatrix}\alpha&\beta\\\beta&0\end{pmatrix}$ of determinant $-\beta^{2}$, hence **indefinite**, and it is **compatible**: the identity $h(xy,z) = h(y,x^{*}z)$ holds, as the remark below records. At $\alpha = 0$, $\beta = 1$ the diagonal values are $h(1+t,1+t) = 2$ and $h(1-t,1-t) = -2$, so the signature is $(1,1)$; the companion form and the fundamental symmetry of *The Fundamental Symmetry of the Form* are those of the example there. The example is the smallest **compatible indefinite** object of the layer, and it is the witness that an indefinite form on an algebra need not fail the compatibility.

**Remark (the compatible forms of the dual numbers).** The compatibility $h(xy,z) = h(y,x^{*}z)$, read entrywise on the basis products, is two real equations on the Hermitian Gram matrix $G$; its solutions are $g_{22} = 0$ and $g_{12}\in\mathbb{R}$, that is the two-parameter family above. Every compatible form on the dual numbers is therefore indefinite, of Gram determinant $-\beta^{2}$, and the definite Hermitian forms are exactly those the compatibility excludes.

### The Semi-Definite Form with Radical

**Example (the dual numbers, a semi-definite form).** On the same algebra take $\alpha = 1$, $\beta = 0$,

$$
h_{0}(a+bt, c+dt) = a\overline{c} .
$$

The form is Hermitian, compatible, positive **semi-definite** and not definite: $h_{0}(t,t) = 0$, and the radical is the ideal $tA = \{bt : b\in\mathbb{C}\}$, of complex dimension one. The diagonal is a seminorm, degenerate exactly on the radical, and the object is the input of *The Completion of a Sesqualgebra with a Form*, §*The Semi-Definite Case and the Radical*: its completion is the definite object $A/tA \cong \mathbb{C}$, the quotient by the closed radical. The example is the witness that the radical of a form of the layer can be a proper nonzero ideal, and that the definiteness asked of the normed object is exactly the vanishing of the radical.

### The Degenerate Form

**Example (the zero form).** Let $A$ be any Banach algebra with a continuous involution and let $h \equiv 0$. The form is Hermitian, compatible and of no definiteness; its radical is the whole of $A$; the diagonal is the zero seminorm; and every operator is self-adjoint and isometric for $h$, so the operator theory of *The Adjoint under a Hermitian Form* is degenerate. The example is the analogue for the form of the degenerate zero product of *Examples of Topological Sesqualgebras*, §*The Degenerate Product*, and it is the witness that nondegeneracy is a hypothesis and not a consequence of the compatibility: nothing in the definition of a sesqualgebra with a form excludes the zero form.

## The Tabulation

### The Table

**Remark (the invariants of the examples).** The tabulation records, for each model, the completeness, the signature or the definiteness class, the compatibility, whether the norm of the form is submultiplicative (a question that arises only for a definite form), the $\mathrm{C}^{*}$-condition (likewise), and the radical. The symbol $\checkmark$ is a yes, $\times$ a no, and $\varnothing$ a question that does not arise, the form defining no norm: an indefinite form, or one whose diagonal is only a seminorm (the semi-definite and zero rows, where the two norm columns do not apply; on the quotient by the radical the induced form is a norm and both conditions hold there).

| object | form | complete | signature | compatible | submult. norm | $\mathrm{C}^{*}$ | radical |
|---|---|---|---|---|---|---|---|
| $\mathbb{C}$ | $z\overline{w}$ | $\checkmark$ | $(2,0)$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $0$ |
| $M_{n}(\mathbb{C})$ | $\operatorname{tr}(XY^{*})$ | $\checkmark$ | $(2n^{2},0)$ | $\checkmark$ | $\checkmark$ | $\times$, $n\geq2$ | $0$ |
| $\mathbb{C}[G]$, $G$ finite | $\sum f\overline{g}$ | $\checkmark$ | $(2\lvert G\rvert,0)$ | $\checkmark$ | $\times$ | $\times$ | $0$ |
| $C(X,\mathbb{C})$ | $\int f\overline{g}\,d\mu$ | $\times$ | $(\infty,0)$ | $\checkmark$ | $\times$ | $\times$ | $0$ |
| $\mathbb{B}$ | $h_{*}$ | $\checkmark$ | $(8,0)$ | $\checkmark$ | $\times$ | $\times$ | $0$ |
| $\mathbb{B}$ | $h_{\natural*}$ | $\checkmark$ | $(2,6)$ | $\times$ | $\varnothing$ | $\varnothing$ | $0$ |
| $\mathbb{C}[t]/(t^{2})$ | $a\overline{d}+b\overline{c}$ | $\checkmark$ | $(1,1)$ | $\checkmark$ | $\varnothing$ | $\varnothing$ | $0$ |
| $\mathbb{C}[t]/(t^{2})$ | $a\overline{c}$ | $\checkmark$ | semi-definite | $\checkmark$ | $\varnothing$ | $\varnothing$ | $tA$ |
| Banach algebra | $0$ | $\checkmark$ | degenerate | $\checkmark$ | $\varnothing$ | $\varnothing$ | $A$ |
| Banach algebra, $*=\mathrm{id}$ | symmetric definite | $\checkmark$ | $(n,0)$ | $\checkmark$ | $\checkmark$ | depends | $0$ |

**Remark (the reading of the table).** The four standard models and the definite biquaternion form are the definite and compatible examples, and the table separates their properties one by one: the $\mathrm{C}^{*}$-condition holds for the field alone among the infinite families and fails for the matrices, the group algebra, the function algebra and the biquaternion trace form, submultiplicativity holds for the field and the matrices and fails for the group algebra, the function algebra and the biquaternion trace form, and completeness fails only for the function algebra. The indefinite rows show the two directions of the independence of definiteness and compatibility: $h_{\natural*}$ is indefinite and not compatible, and the dual-number form is indefinite and compatible. The semi-definite and degenerate rows show the first way in which a form can fail to define a norm of the layer: by a nonzero radical, as for $h_{0}$ and the zero form, and by being indefinite, as for the dual-number form and $h_{\natural*}$. In every nondegenerate definite example the norm of the form is the Euclidean norm of the coordinates in an orthogonal basis; the $\mathrm{C}^{*}$-condition fails at the unit for the matrix trace form, $\lVert 1\rVert^{2} = n$ against $\lVert 1^{*}1\rVert = \sqrt{n}$ for $n \geq 2$, and at the zero divisor $1 + \mathrm{i}e_{1}$ for the biquaternion trace form, $\lVert P^{*}P\rVert = 2\sqrt{2}$ against $\lVert P\rVert^{2} = 2$.

### The Collapse at the Identity

**Theorem (the collapse of the layer with a form).** Let $A$ be an example with $\varsigma = \mathrm{id}$. Then the form is symmetric and $R$-bilinear, the compatibility is the identity $h(xy,z) = h(y,xz)$, the diagonal is a quadratic form and the norm of the form is the norm of a symmetric positive definite form; the examples are those of *Topological Algebras and Banach Algebras* with a symmetric definite form, the bilinear counterpart of the table being the Hilbert algebras of *Hilbert Algebras* and the symmetric forms of *Isometries and Orthogonal Transformations*. If in addition $* = \mathrm{id}$ then the derived product is the algebra product, the left multiplications are self-adjoint, and the object is a normed or Banach algebra with a symmetric definite form.

*Proof.* At $\varsigma = \mathrm{id}$ the semilinear slots are linear, the twists vanish, and each row of the table is the corresponding statement of the bilinear layer; the identification is the collapse theorem of *Topological Sesqualgebras with a Form*, §*The Collapse at the Trivial Involution*, and the norm statements are those of *The Norm Defined by a Form*, §*The Collapse at the Trivial Involution*. $\square$

**Remark (the collapse in the table).** The rows whose base involution is the conjugation — the complex field, the matrices, the complex group and function algebras, the two biquaternion forms and the dual numbers — do not collapse: their forms are sesquilinear, their norms scale by the modulus, and their derived products are the nontrivial ones of the layer. The rows with a trivial involution collapse: a Banach algebra with $* = \mathrm{id}$ and a symmetric definite form is an object of *Topological Algebras and Banach Algebras* with a symmetric form, of the kind studied in *Hilbert Algebras* and *Bilinear Forms*. The intermediate case of the layer, the base collapsed with $\varsigma = \mathrm{id}$ and $*$ nontrivial, is not among the rows: its examples are the real matrices with the transpose and the quaternions with the conjugation of *Examples of Topological Sesqualgebras*, whose forms are the symmetric ones of the bilinear layer.

## Summary

The examples of the layer with a form are the associative algebras with an involution of *Examples of Topological Sesqualgebras*, each with a compatible Hermitian form, and the tabulation separates the hypotheses that the definitions do not. The **four standard models** — the field $\mathbb{C}$ with $h(z,w) = z\overline{w}$, the matrices with the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$, the group algebra with the $L^{2}$ form $\sum f\overline{g}$, and the function algebra with the $L^{2}$ form $\int f\overline{g}$ — are definite and compatible, and they separate **completeness** (failing only for the function algebra), **submultiplicativity** (failing for the group algebra and the function algebra) and the **$\mathrm{C}^{*}$-condition** (holding only for the field among them). The **biquaternion algebra** carries a definite compatible form $h_{*}$ of signature $(8,0)$ and an indefinite form $h_{\natural*}$ of signature $(2,6)$ that is **not** compatible, so definiteness and compatibility are independent; the **dual numbers** carry an indefinite compatible form of signature $(1,1)$ and a semi-definite form with radical $tA$, so a compatible form can be indefinite and a definite-looking diagonal can have a radical; and the **zero form** has radical the whole algebra and is the witness that nondegeneracy is assumed and not derived. In every definite nondegenerate example the norm of the form is the Euclidean norm in an orthogonal basis, the $\mathrm{C}^{*}$-condition fails at the unit for the matrix trace form and at the zero divisor $1 + \mathrm{i}e_{1}$ for the biquaternion trace form, and the radical vanishes exactly for the nondegenerate forms, which is the hypothesis under which the completion of *The Completion of a Sesqualgebra with a Form* is a completion in the layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(xy,z) = h(y,x^{*}z)$ | the compatibility, the condition the forms of the layer satisfy |
| $h(z,w) = z\overline{w}$ on $\mathbb{C}$ | the field, definite, submultiplicative, $\mathrm{C}^{*}$ |
| $h(X,Y) = \operatorname{tr}(XY^{*})$ | the trace form, Frobenius norm, no $\mathrm{C}^{*}$-condition |
| $h(f,g) = \sum f\overline{g}$ | the $L^{2}$ form of the group algebra, complete, not submultiplicative |
| $h(f,g) = \int f\overline{g}\,d\mu$ | the $L^{2}$ form of the function algebra, incomplete |
| $h_{*}(P,Q) = \operatorname{Sc}(PQ^{*})$ | the biquaternion definite form, signature $(8,0)$ |
| $h_{\natural*}(P,Q) = \operatorname{Sc}(P^{\natural}Q^{*})$ | the biquaternion indefinite form, signature $(2,6)$, not compatible |
| $h(a+bt,c+dt) = \alpha a\overline{c}+\beta(a\overline{d}+b\overline{c})$ | the dual-number family, indefinite and compatible |
| $h_{0}(a+bt,c+dt) = a\overline{c}$ | the semi-definite form, radical $tA$ |
| $h \equiv 0$ | the degenerate form, radical $A$ |
| $\varnothing$ | a question that does not arise for an indefinite or degenerate form |

## Further Reading

- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the Banach algebras, their involutions and the submultiplicative norms of the examples.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume I* (Cambridge University Press, 1994), for the group algebras, the $\mathrm{C}^{*}$-algebras and the distinction between the $\mathrm{C}^{*}$-norm and the other algebra norms.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the Hilbert algebras, the $L^{2}$ forms of the group algebra and the function algebra, and the boundedness of the multiplications.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the trace form, the Frobenius norm and the $\mathrm{C}^{*}$-identity of the matrix algebras.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the indefinite forms, the signatures and the fundamental symmetry of the dual-number example.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the Hermitian forms over a field with involution, their Gram matrices, their radicals and their quotients.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the Hermitian forms on an algebra with involution and the compatibility with the product.
