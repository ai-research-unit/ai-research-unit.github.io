# __The First-Order Root of the Biquaternion D'Alembertian__

## Introduction

The d'Alembertian of the biquaternion algebra is the scalar second-order operator

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla\bigr)
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q ,
$$

the quaternionic norm of the gradient. On the material sector, where $Q_t=iq'_t$, the same operator is

$$
\Box=-\frac{\partial^2}{\partial (q'_t)^2}+\Delta .
$$

Every derivative in this article is the corpus gradient. With the units $e_t,\vec e_x,\vec e_y,\vec e_z$ and the coordinates $Q_\mu$,

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla ,
$$

with $\Delta_Q=\sum_{k\in\{x,y,z\}}\partial^2/\partial Q_k^2$ and $\varepsilon=(1,-1,-1,-1)$. The gradient is an element with derivative coefficients, and it multiplies its argument on the left. No other letter names it.

This article asks for a first-order operator $D$ whose square is $\Box-\lambda$, or for a factorisation of $\Box-\lambda$ into two first-order operators. The two answers differ. A **single square** is one first-order operator $D$ with $D^2=(\Box-\lambda)e_t$, where both $D$ and its coefficients are read in the algebra; if it existed, its kernel would sit inside the second-order solution space. A **factorisation** is a product $D_-D_+$ of two first-order operators, each a left multiplication by an element with derivative coefficients, whose product is $(\Box-\lambda)e_t$. At $\lambda=0$ the algebra supplies it with $D_+=\tilde\nabla$ and $D_-=\tilde\nabla^{\natural}$. When the two factors are distinct, the two first-order equations together are equivalent to the second-order equation.

**The results.** The algebra admits the factorisation and not the single square. A scalar square needs four elements of $\mathbb{B}$ that anticommute pairwise, with squares $+e_t$ and $-e_t$ in the ratio one to three. The algebra supplies the three of the minus sign, the spatial units $\vec e_k$, and no fourth: the three generate $\mathbb{B}$, and an element that anticommutes with all three is zero. The obstruction sits in the second order, where the zero-order term cannot reach, so no constant-coefficient first-order operator with element coefficients has a scalar square. The gradient is the first-order operator of the algebra. Its square carries a vector remainder, while its product with the conjugate is $\Box$. The free equation stays first order in one field, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$. The massive equation is the chiral pair

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R},
\qquad \lambda=m^2 .
$$

On the doubled carrier $\mathbb{B}\oplus\mathbb{B}$ the pair operator $\mathbb{D}$ satisfies $\mathbb{D}^2=\Box I$, and the mass is its shift, $(\mathbb{D}-m)(\mathbb{D}+m)=(\Box-m^2)I$.

**The two matrix sizes.** The biquaternion algebra is $\mathbb{B}\cong M_2(\mathbb{C})$ (*The Polarized Module of the Biquaternion Algebra*). A field of this article is an element of that algebra, four complex dimensions. The gradient takes values in the algebra, and the d'Alembertian is its scalar norm. The operator algebra $\mathrm{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ is the algebra of maps of that field; it is not a second representation of $\mathbb{B}$, and this article uses no matrix carrier. A first-order root with matrix coefficients would be a map outside the algebra and outside the one-sided calculus.

The article is mathematics. The d'Alembertian is the norm of the gradient; the mass is the name of the shift parameter, and no other physical interpretation is used. **The two letters are the two factors.** In this article $L$ and $R$ name the field of the first factor and the field of the second, which are related by left multiplications and therefore carry one and the same value of the chirality test; they name the two *values* of that test in the two-sided writing of the physics corpus, where the operator carries a right slot as well. The two uses of the letters are told apart by the operator, not by the letters. The conventions are those of *Algebra and Element Conventions* and *Operator and Calculus Conventions*; the calculus is one-sided, and every equation is written on the left.

## The D'Alembertian and Its Symbol

### The Algebra and the Gradient

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, where $e_t=1$ is the scalar unit and the three vector units satisfy $\vec e_k^2=-e_t$ and the quaternion relations. A general element is

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu ,
$$

with complex coefficients $Q_\mu$. The gradient and its conjugate are the two operators of the introduction. On the material sector, where $Q_t=iq'_t$, the derivative along the fourth coordinate reads $\partial/\partial Q_t=-i\,\partial/\partial q'_t$.

The d'Alembertian is scalar: it multiplies by $e_t$ and acts coefficient by coefficient. **The d'Alembertian is not the partner operator.** The plain bilinear norm of the gradient is $\partial^2/\partial Q_t^2-\Delta_Q$, a different operator, and its root is a different problem. This article treats $\Box$ only. The two operators are distinguished in *Operator and Calculus Conventions*, and the distinction is fixed by the form, not by a choice of sign.

### The Symbol

On a plane wave $\exp\bigl(i(q_0x_0-\vec q\cdot\vec x)\bigr)$, where $x_0=q'_t$ and $x_k=Q_k$, the substitution is $\partial/\partial Q_t\mapsto q_0$ and $\partial/\partial Q_k\mapsto-iq_k$. The symbol of the gradient is left multiplication by the element

$$
\tilde K=q_0e_t-i\sum_k q_k\vec e_k=q_0-i\vec q ,
\qquad
\tilde K^{\natural}=q_0+i\vec q ,
$$

and its quaternionic norm is

$$
\tilde K^{\natural}\tilde K=\tilde K\tilde K^{\natural}=\bigl(q_0^2-\lvert\vec q\rvert^2\bigr)e_t .
$$

The same expression is the symbol of $\Box$, because $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla$. The square of the symbol is not scalar:

$$
\tilde K^2=\bigl(q_0^2+\lvert\vec q\rvert^2\bigr)e_t-2iq_0\vec q .
$$

The mass shell is the quadric $q_0^2-\lvert\vec q\rvert^2=\lambda$; at $\lambda=0$ it is the null cone of the quaternionic norm.

**The zero divisor on the cone.** Off the cone, $\tilde K$ is a unit, with inverse $\tilde K^{\natural}/(\tilde K^{\natural}\tilde K)$, and the map $\tilde{Ξ}\mapsto\tilde K\tilde{Ξ}$ is invertible. On the cone the norm vanishes and $\tilde K$ is a zero divisor. In the representation $\mathbb{B}\cong M_2(\mathbb{C})$ the determinant of an element is its quaternionic norm, so a nonzero null element is a matrix of rank one, and left multiplication by a rank-one matrix has rank two. For a nonzero null covector the map $\tilde{Ξ}\mapsto\tilde K\tilde{Ξ}$ therefore has rank two and a two-dimensional kernel. The free equation $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$ has a nonzero plane-wave solution exactly on the cone, and it selects two of the four complex dimensions there.

### The Square of the Gradient

Because the partial derivatives commute,

$$
\tilde\nabla^2=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q+2\sum_k\vec e_k\frac{\partial^2}{\partial Q_t\,\partial Q_k}.
$$

The square is the partner operator plus the mixed term, and both separate it from $\Box$. The three spatial units anticommute in pairs and square to $-e_t$, so the spatial part of the square is scalar. The time unit does not join them: $e_t$ is the identity of the algebra, so it commutes with every spatial unit, and the two orders of $\partial^2/\partial Q_t\partial Q_k$ add instead of cancelling. The time coefficient of the gradient is the identity, and nothing anticommutes with the identity.

On the material sector, where $Q_t=ix_0$ and $\partial/\partial Q_t=-i\,\partial/\partial x_0$, the same operator is

$$
\tilde\nabla^2=\Box-2\Delta-2i\sum_k\vec e_k\frac{\partial^2}{\partial x_0\,\partial x_k}.
$$

**The product with the conjugate is scalar.** Read on the units, the two operators differ only by the sign of the three spatial terms, and the product is central because $\varepsilon_\mu e_\mu^2=\varepsilon_\mu^2e_t=e_t$ for every $\mu$:

$$
\tilde\nabla^{\natural}\tilde\nabla=\tilde\nabla\tilde\nabla^{\natural}=\Box .
$$

## The Clifford Obstruction

### The Three Spatial Units

**Proposition.** The elements $\vec e_k$, $k=x,y,z$, satisfy

$$
\vec e_k^2=-e_t,\qquad \{\vec e_j,\vec e_k\}=0\quad(j\ne k).
$$

They generate $\mathbb{B}$ itself.

*Proof.* The square is $\vec e_k^2=-e_t$. For $j\ne k$ the product is $\vec e_j\vec e_k$, and the anticommutator is $\{\vec e_j,\vec e_k\}=0$. The three generators and their products span the four-dimensional algebra $\mathbb{B}$.

### No Fourth Element

**Proposition.** No element $X\in\mathbb{B}$ anticommutes with all three $\vec e_k$.

*Proof.* Write $X=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. The anticommutator with $\vec e_x$ is

$$
\{X,\vec e_x\}=2a_t\vec e_x-2a_x e_t ,
$$

so $a_t=a_x=0$. The anticommutator with $\vec e_y$ then gives $a_y=0$, and $X=a_z\vec e_z$ commutes with $\vec e_z$, so $a_z=0$. Hence $X=0$.

The proposition is stated for the three spatial units. It holds for every quaternionic triple: if $b_k$ satisfy $b_k^2=-e_t$ and pairwise anticommutation, they generate $\mathbb{B}$, and an element that anticommutes with all three lies in the commutant of $\mathbb{B}$, which is $\mathbb{C}e_t$; since $e_t$ commutes, it is zero.

### No Single Square

**Theorem.** Let $D=\sum_\mu a_\mu\partial/\partial Q_\mu+b$ with $a_\mu,b\in\mathbb{B}$ constant. Then $D^2$ is not $(\Box-\lambda)e_t$ for any $\lambda\in\mathbb{C}$.

*Proof.* Because the partial derivatives commute, the second-order part of $D^2$ is

$$
\frac12\sum_{\mu,\nu}\bigl(a_\mu a_\nu+a_\nu a_\mu\bigr)\frac{\partial^2}{\partial Q_\mu\partial Q_\nu}.
$$

Matching it to $(\Box-\lambda)e_t=\sum_\mu\partial^2/\partial Q_\mu^2-\lambda e_t$ gives

$$
a_\mu a_\nu+a_\nu a_\mu=2\delta_{\mu\nu}e_t .
$$

In particular the three spatial coefficients anticommute pairwise and square to $e_t$. Multiply them by the central $i$: the three $c_k=ia_k$ anticommute pairwise and square to $-e_t$. They form a quaternionic triple, so they generate $\mathbb{B}$, and no element anticommutes with all three. Hence no $a_t$ anticommutes with all three $a_k$, and the relation $a_ta_k+a_ka_t=0$ is impossible for a nonzero $a_t$. The zero-order term $b$ enters only the first-order and constant parts, $\sum_\mu(a_\mu b+ba_\mu)\partial/\partial Q_\mu+b^2$, and cannot repair the second order. The contradiction is therefore independent of $b$ and $\lambda$.

The same argument covers the material-sector signature. Multiplying every coefficient by $i$ flips the sign of every square and preserves every anticommutator, so a quadruple of one signature exists exactly when one of the opposite signature does.

### The Carrier Is Four-Dimensional

A field that carries the four units is an element of $\mathbb{B}$, four complex dimensions. The gradient has four coefficients, one per unit, and it acts on the four coefficients of the field. A field whose value is one complex number has no first-order equation of the series: $\tilde\nabla\tilde{Ξ}=0$ reads

$$
\tilde\nabla\tilde{Ξ}=\sum_\mu e_\mu\frac{\partial\tilde{Ξ}}{\partial Q_\mu}=0,
$$

and the four units are independent, so all four partial derivatives vanish and the field is constant.

The carrier of a first-order operator with element coefficients is therefore $\mathbb{B}$, and it is not enlarged by the root. The root changes the action, not the carrier. A larger carrier would require coefficients that are maps of the carrier, not elements of $\mathbb{B}$; those maps lie outside the one-sided calculus, and this article does not use them.

## The Factorisation

### The Two Factors

The product of the gradient and its conjugate is the d'Alembertian:

$$
\tilde\nabla^{\natural}\tilde\nabla=\tilde\nabla\tilde\nabla^{\natural}=\Box .
$$

The identity is exact, and it is the whole factorisation of $\Box$ that the algebra supplies. Each factor is left multiplication by an element with derivative coefficients, and the product is composition on the field: the right factor acts first, the left factor acts on the result, and no derivative acts on a coefficient, since all coefficients are constant. The factorisation has two factors, and neither is a root by itself: the square of either one alone carries the vector remainder of §*The Square of the Gradient*. That is the sense in which the root exists: as a pair of first-order operators, not as one operator.

### The Pair Operator

The two equations of the massive case are one operator on $\mathbb{B}\oplus\mathbb{B}$. Write $\tilde{Ξ}_{\mathrm{sp}}=(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})$ and

$$
\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}=\bigl(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\ \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}\bigr).
$$

Then

$$
\mathbb{D}^2=\Box I,
\qquad
(\mathbb{D}-m)(\mathbb{D}+m)=\bigl(\Box-m^2\bigr)I .
$$

The pair is $(\mathbb{D}-m)\tilde{Ξ}_{\mathrm{sp}}=0$. The operator $\mathbb{D}$ is the pair operator on $\mathbb{B}\oplus\mathbb{B}$ of the conventions; it is a map of the doubled carrier and not an element of $\mathbb{B}$.

### The Chiral Pair

The two parts are two fields, $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$, written together as $\tilde{Ξ}_{\mathrm{sp}}=(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})$; each is an element of $\mathbb{B}$ and no relation between them is assumed in advance. The massive equation is the pair

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R} .
$$

Substituting the first relation into the second gives $\tilde\nabla^{\natural}\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m^2\tilde{Ξ}_{\mathrm{sp},R}$, that is

$$
\Box\tilde{Ξ}_{\mathrm{sp},R}=m^2\tilde{Ξ}_{\mathrm{sp},R} ,
$$

and the first relation then defines $\tilde{Ξ}_{\mathrm{sp},L}=m^{-1}\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}$. Each part satisfies the shifted d'Alembertian, and the pair is a bijection with the second-order solutions of one part, not a new restriction. At $m=0$ the two relations decouple: $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$.

The two labels $L$ and $R$ are the two slots of the pair. They are not the eigenspaces of a chirality: the chirality is the right action

$$
\tilde{Ξ}\longmapsto-i\tilde{Ξ}\vec e_z=i\tilde{Ξ}\omega ,
$$

where $\omega=-\vec e_z$ is the pseudoscalar, $\omega^2=-e_t$. The right action has square the identity, and its two eigenspaces are the two chiral halves: $\tilde{Ξ}\vec e_z=i\tilde{Ξ}$ for the eigenvalue $+1$ and $\tilde{Ξ}\vec e_z=-i\tilde{Ξ}$ for the eigenvalue $-1$. It commutes with every left multiplication, so it commutes with the gradient and preserves each kernel; at a nonzero null covector the two-dimensional kernel carries one state of each chirality. The mass couples the two labels, and because the gradient preserves the chirality, each label-$L$ part and its label-$R$ partner carry the same chirality; the pair does not exchange the two chiralities. The corpus calculus writes every equation on the left, so the right action is used here only to label the halves; it is a single right action, not a two-sided operator.

### The Determinant

On a plane wave each derivative is replaced by its symbol, and $\mathbb{D}$ becomes the block matrix

$$
\mathbb{D}(\tilde K)=
\begin{pmatrix}0&\tilde K\\ \tilde K^{\natural}&0\end{pmatrix},
\qquad
\mathbb{D}(\tilde K)(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})=\bigl(\tilde K\tilde{Ξ}_{\mathrm{sp},R},\ \tilde K^{\natural}\tilde{Ξ}_{\mathrm{sp},L}\bigr),
$$

whose off-diagonal entries are the left multiplications $\tilde{Ξ}\mapsto\tilde K\tilde{Ξ}$ and $\tilde{Ξ}\mapsto\tilde K^{\natural}\tilde{Ξ}$. Every entry is a left multiplication by an element, and the matrix is a map of $\mathbb{B}\oplus\mathbb{B}$. Its determinant is

$$
\det\bigl(\mathbb{D}(\tilde K)-m\bigr)
=\bigl(q_0^2-\lvert\vec q\rvert^2-m^2\bigr)^4 ,
$$

the fourth power of the symbol of $\Box-m^2$. The fourth power is the signature of the doubled carrier: eliminating one block leaves the Schur complement $(q_0^2-\lvert\vec q\rvert^2-m^2)$ times the four-dimensional identity.

The determinant of the left action of $\tilde K$ on $\mathbb{B}$ is the square of its quaternionic norm,

$$
\det\bigl(\tilde{Ξ}\mapsto\tilde K\tilde{Ξ}\bigr)
=\bigl(\tilde K^{\natural}\tilde K\bigr)^2
=\bigl(q_0^2-\lvert\vec q\rvert^2\bigr)^2 ,
$$

because the determinant of the left regular matrix of an element is the square of its norm (*The Polarized Module of the Biquaternion Algebra*). The two identities are consistency checks. A determinant identity is not a square root: it says that a power of the scalar symbol is the determinant of a first-order operator, not that one first-order operator has the scalar as its square.

## The Classification of Fields

| field | first-order equation | root? |
|---|---|---|
| one complex number | $\tilde\nabla\tilde{Ξ}=0$, which forces $\partial\tilde{Ξ}/\partial Q_\mu=0$ | no, it forces a constant |
| element of $\mathbb{B}$, massless | $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$ | yes, one factor of $\Box$ |
| element of $\mathbb{B}$, massive | the pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R}$ | yes, the pair |

**The scope.** The table classifies the fields on which the constant-coefficient first-order ansatz of this article can be solved. It is not a classification of all first-order operators whose square is scalar. A first-order operator with matrix coefficients, or with a non-constant coefficient, is outside the article. The free equation stays first order in one field, and the mass is carried by the pair; no single field carries a scalar mass.

## Worked Examples

**A plane wave.** Let $\tilde{Ξ}(x)=\exp\bigl(i(q_0x_0-\vec q\cdot\vec x)\bigr)v$ with $v\in\mathbb{B}$ constant. Then

$$
\tilde\nabla\tilde{Ξ}=\tilde K\tilde{Ξ},
\qquad
\Box\tilde{Ξ}=\bigl(q_0^2-\lvert\vec q\rvert^2\bigr)\tilde{Ξ} .
$$

The free equation has a nonzero solution exactly when $\tilde K$ is a zero divisor, that is on the cone $q_0^2-\lvert\vec q\rvert^2=0$. At a nonzero null covector the map $\tilde{Ξ}\mapsto\tilde K\tilde{Ξ}$ has rank two, and the solution space is two-dimensional.

**A constant element.** A constant $v\in\mathbb{B}$ satisfies $\tilde\nabla v=0$ and $\Box v=0$. The example shows that the free equation has a nontrivial kernel already at $\lambda=0$. The constant part of the kernel is all of $\mathbb{B}$, the degenerate case of the cone at $q=0$; at a nonzero null covector the kernel is two-dimensional, one state of each chirality.

**Promotion of a solution.** Let $\tilde{Ξ}_{\mathrm{sp},R}$ solve $(\Box-m^2)\tilde{Ξ}_{\mathrm{sp},R}=0$ with $m\ne0$, and put $\tilde{Ξ}_{\mathrm{sp},L}=m^{-1}\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}$. Then

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=\frac1m\Box\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},R},
$$

so the pair is satisfied. The example exhibits the bijection between the solutions of the shifted d'Alembertian on one part and the solutions of the pair.

**The determinant.** For the symbol $\tilde K$, the determinant of the left action is $(q_0^2-\lvert\vec q\rvert^2)^2$, and the determinant of the pair operator shifted by $m$ is $(q_0^2-\lvert\vec q\rvert^2-m^2)^4$. At $q=(2,1,0,0)$ the norm is $3$, the first determinant is $9$, and at $m=1$ the second determinant is $(3-1)^4=16$.

## Verification

The identities were recomputed before they were written. The algebra multiplication and the left action were built as four-dimensional complex matrices, and the symbol reductions were checked at random covectors. The residuals are the largest absolute difference over the stated samples.

| check | result |
|---|---|
| $\tilde K^{\natural}\tilde K-(q_0^2-\lvert\vec q\rvert^2)e_t$ on $100$ random covectors | $8.9\times10^{-16}$ |
| $\tilde K^2-\bigl((q_0^2+\lvert\vec q\rvert^2)e_t-2iq_0\vec q\bigr)$ on $100$ random covectors | $3.6\times10^{-15}$ |
| rank and kernel of $\tilde{Ξ}\mapsto\tilde K\tilde{Ξ}$ at five nonzero null covectors | rank $2$, kernel $2$ |
| the same off the cone, at $q=(2,1,0,0)$ | rank $4$ |
| $\det(\tilde{Ξ}\mapsto\tilde K\tilde{Ξ})-(q_0^2-\lvert\vec q\rvert^2)^2$ on $100$ random covectors | $1.2\times10^{-13}$ |
| no element anticommutes with the three spatial units | kernel dimension $0$ |
| the same for $100$ generic quaternionic triples | kernel dimension $0$ |
| $\mathbb{D}(\tilde K)^2-\Box I$ on $100$ random covectors | $3.6\times10^{-15}$ |
| $\det(\mathbb{D}(\tilde K)-m)-(q_0^2-\lvert\vec q\rvert^2-m^2)^4$ on $100$ random covectors | $1.8\times10^{-10}$ |
| the chirality $\tilde{Ξ}\mapsto-i\tilde{Ξ}\vec e_z$ on the null kernel | eigenvalues $+1$ and $-1$, one each |

The numerical checks are checks of polynomial identities at random points. The proof is the algebra of the preceding sections; the numbers guard against a sign or factor error in the transcription.

## Summary

The d'Alembertian $\Box=\partial^2/\partial Q_t^2+\Delta_Q=-\partial^2/\partial(q'_t)^2+\Delta$ is the quaternionic norm of the gradient and a scalar second-order operator. The algebra admits no single first-order root: a scalar square needs four elements that anticommute pairwise, one of square $+e_t$ and three of square $-e_t$, the algebra supplies the three spatial units, and no fourth element anticommutes with all three. The obstruction sits in the second order, where the zero-order term cannot reach.

The first-order operator of the algebra is the gradient. Its square is not scalar, because $e_t$ is the identity and commutes with the three spatial units, so the mixed derivatives add. Its product with the conjugate is $\Box$, and that product is the factorisation of the d'Alembertian that the algebra supplies. The free equation is first order in one field, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$; at a nonzero null covector it selects two of the four complex dimensions of the second-order solution space, one state of each chirality.

The mass is a central scalar, and a central scalar commutes with every derivative. A scalar zero-order term therefore changes only the constant term of a square; it cannot remove the vector remainder of $\tilde\nabla^2$, so no scalar shift makes the gradient square to $\Box$. The mass acts instead as the coupling of the two parts, and the pair operator $\mathbb{D}$ carries it, with $(\mathbb{D}-m)(\mathbb{D}+m)=(\Box-m^2)I$. Eliminating one member returns $\Box\tilde{Ξ}_{\mathrm{sp},R}=m^2\tilde{Ξ}_{\mathrm{sp},R}$, so the pair and the second-order equation on one part are equivalent.

The determinant of the left action of the symbol is the square of the quaternionic norm, and the determinant of the pair operator is the fourth power of the symbol of $\Box-m^2$. A determinant identity is not a square root. The results are a classification of form, and no mass, coupling or dynamics is predicted.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | the biquaternionic gradient, an element with derivative coefficients, acting on the left |
| $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial Q_\mu$ | its quaternion conjugate, the second factor of $\Box$ |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$ | the d'Alembertian, $\partial^2/\partial Q_t^2+\Delta_Q$ |
| $\mathrm{Sc}$ | the scalar part of an element, its coefficient of $e_t$ |
| $Q_\mu$ | the algebra coordinates, $Q_t=iq'_t$ |
| $x_\mu=(q'_t,x,y,z)$ | the real coordinates |
| $q_\mu$ | the wave covector of a plane wave |
| $\vec e_k$ | the three spatial units, $\vec e_k^2=-e_t$ |
| $\omega=-\vec e_z$ | the pseudoscalar, $\omega^2=-e_t$ |
| $\tilde K=q_0-i\vec q$ | the symbol of the gradient |
| $\lambda$, $m$ | the shift and the mass, $\lambda=m^2$ |
| $\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}$ | the two slots of the pair, each an element of $\mathbb{B}$ |
| $I$ | the identity map of the carrier, an operator and not an element |
| $\mathbb{D}$ | the pair operator on $\mathbb{B}\oplus\mathbb{B}$, $\mathbb{D}(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})=(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L})$, with $\mathbb{D}^2=\Box I$ |
| $\tilde{Ξ}\mapsto-i\tilde{Ξ}\vec e_z$ | the chirality, a single right multiplication; its eigenspaces are $\tilde{Ξ}\vec e_z=\pm i\tilde{Ξ}$ |

## Further Reading

- [Conventions in Mathematics](algebra-and-element-conventions.html), for the derivative conventions and the gradient.
- [Biquaternion Analysis](biquaternion-analysis.html), for the gradient, its conjugate and the d'Alembertian at length.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the four forms, the four norms and the definition of the d'Alembertian.
- [The Polarized Module of the Biquaternion Algebra](the-polarized-module-of-the-biquaternion-algebra.html), for the target representation of the algebra and the determinant of the left regular matrix.
