# __The First-Order Root of the Biquaternion D'Alembertian__

## Introduction

The d'Alembertian of the biquaternion algebra is the scalar second-order operator

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla\bigr)
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q ,
$$

the quaternionic norm of the gradient. On the material sector $\mathbb{M}_-$, where $Q_t=iq'_t$, the same operator is

$$
\Box=-g^{\mu\nu}\partial_\mu\partial_\nu
=-\frac{\partial^2}{\partial(q'_t)^2}+\Delta ,
\qquad
g=\mathrm{diag}(+1,-1,-1,-1).
$$

This article works in the real coordinates $x^\mu=(q'_t,x,y,z)$; the $Q$ form is the Euclidean transcription, with $\partial_{Q_t}=-i\partial_{q'_t}$. This article asks for a first-order operator $D$ whose square is $\Box$, or the shifted operator $\Box-\lambda$ for a complex number $\lambda$.

The question has two answers, and they are different. A **single square** is one first-order operator $D$ with $D^2=(\Box-\lambda)I$. A **factorisation** is a product $D_-D_+=(\Box-\lambda)I$ of two first-order operators. The single square is the stronger equation: its kernel is a chiral half of the second-order solution space. The factorisation is the weaker pair: when the two factors are distinct, the two first-order equations together are equivalent to the second-order equation. At $\lambda=0$ the two coincide at the level of the operator, but the kernel of the root is still a half. A **Clifford root** is a first-order operator of the form $D=i\sum_\mu\gamma_\mu\partial_\mu+B$ with constant matrices $\gamma_\mu,B$; this article classifies the Clifford roots.

**The results.** The d'Alembertian has no Clifford root on the two-dimensional simple module of $\mathbb{B}$. The minimal carrier is four-dimensional, the regular module $\mathbb{B}\cong S_+\oplus S_-$. The three elements $\vec e_k$ supply a three-generator Clifford system inside the algebra; the fourth generator is not a left multiplication by an element of $\mathbb{B}$, but the two-sided direction that exchanges the two minimal left ideals. On the regular module the unshifted cell root is $\mathsf D=i\sum_\mu\gamma_\mu\partial_\mu$, with $\mathsf D^2=\Box I$. The coefficients of $\mathsf D$ are cells of the enveloping algebra $\mathbb{B}^{\mathrm e}$, not elements of $\mathbb{B}$; the biquaternion object is the gradient, and the biquaternion factorisation of the unshifted operator is $\tilde\nabla\tilde\nabla^{\natural}=\Box$. The single square is the cell root. The shifted operator has a single root exactly when the zero-order term is a pseudoscalar $c\gamma_5$ with $c^2=-\lambda$; a scalar shift admits only the factorisation $(\mathsf D-\kappa)(\mathsf D+\kappa)$.

**The two matrix sizes.** The biquaternion algebra is $\mathbb{B}\cong M_2(\mathbb{C})$ (*$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*). The gradient takes values in that algebra, and the d'Alembertian is its scalar norm; the target representation is $M_2(\mathbb{C})$, not $M_4(\mathbb{C})$. The four-dimensional space of this article is the regular module $\mathbb{B}$, on which the algebra acts by left multiplication. The $M_4(\mathbb{C})$ that appears below is the algebra of **operators** on that module, the enveloping algebra $\mathbb{B}^{\mathrm e}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, not a second representation of $\mathbb{B}$. The distinction is the reason the root is two-sided: the d'Alembertian is a scalar operator read in the algebra, while the root lives in the operator algebra of the regular module.

The article is mathematics. The d'Alembertian is the norm of the gradient, and no physical interpretation is used. The conventions are those of *Algebra and Element Conventions* and *Operator and Calculus Conventions*; the two-sided operators are *Two-Sided Operators on the Biquaternion Algebra* and *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the minimal left ideals are *The Minimal Left Ideals* and *Spinors as Peirce Coordinates in the Biquaternion Algebra*.

## The D'Alembertian and Its Symbol

### The Algebra and the Gradient

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, where $e_t=1$ is the scalar unit and the three vector units satisfy $\vec e_k^2=-e_t$ and the quaternion relations. A general element is

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu ,
$$

with complex coefficients $Q_\mu$. The coordinate derivative is written $\partial/\partial Q_\mu$, and the derivative along the fourth coordinate is $\partial/\partial Q_t$; on the material sector, where $Q_t=iq'_t$, it reads $\partial/\partial Q_t=-i\,\partial/\partial q'_t$. The biquaternionic gradient is

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu} ,
$$

and its quaternion conjugate is

$$
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \varepsilon=(1,-1,-1,-1).
$$

The d'Alembertian is the quaternionic norm of the gradient,

$$
\Box=\langle\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla\bigr)
=\mathrm{Sc}\bigl(\tilde\nabla\tilde\nabla^{\natural}\bigr)
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q ,
$$

with $\Delta_Q=\sum_{k\in\{x,y,z\}}\partial^2/\partial Q_k^2$. The operator is scalar: it multiplies by $e_t$ and acts coefficient by coefficient.

**The d'Alembertian is not the partner operator.** The plain bilinear norm of the gradient is $\partial^2/\partial Q_t^2-\Delta_Q$, a different operator, and its root is a different Clifford system. This article treats $\Box$ only. The two operators are distinguished in *Operator and Calculus Conventions*, and the distinction is fixed by the form, not by a choice of sign.

### The Symbol

For a constant-coefficient operator, the **symbol** is the matrix polynomial obtained by replacing $i\partial_\mu$ by a complex variable $q_\mu$, equivalently $\partial_\mu$ by $-iq_\mu$. The symbol of $\Box$ is

$$
\sigma(\Box)(q)=g^{\mu\nu}q_\mu q_\nu=q_0^2-q_1^2-q_2^2-q_3^2 ,
$$

and the symbol of a first-order operator

$$
D=i\sum_{\mu\in\{t,x,y,z\}}\gamma_\mu\frac{\partial}{\partial x^\mu}+B,
\qquad \gamma_\mu,B\in M_n(\mathbb{C})\ \text{constant},
$$

is

$$
\sigma(D)(q)=\sum_{\mu\in\{t,x,y,z\}}q_\mu\gamma_\mu+B .
$$

For constant coefficients the symbol of a composition is the product of the symbols, so $\sigma(D^2)(q)=\sigma(D)(q)^2$. The operator identity $D^2=(\Box-\lambda)I_n$ is therefore equivalent to the matrix identity

$$
\Bigl(\sum_\mu q_\mu\gamma_\mu+B\Bigr)^2
=\Bigl(g^{\mu\nu}q_\mu q_\nu-\lambda\Bigr)I_n
$$

for every $q\in\mathbb{C}^4$.

**Proposition (the root condition).** Let $D=i\sum_\mu\gamma_\mu\partial_\mu+B$ with constant $\gamma_\mu,B\in M_n(\mathbb{C})$. Then $D^2=(\Box-\lambda)I_n$ if and only if

$$
\boxed{\;\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_n,\qquad
\{\gamma_\mu,B\}=0\quad\text{for every }\mu,\qquad
B^2=-\lambda I_n.\;}
$$

*Proof.* Expanding the square gives

$$
D^2=-g^{\mu\nu}\frac{\partial^2}{\partial x^\mu\partial x^\nu}
+i\sum_\mu\{\gamma_\mu,B\}\frac{\partial}{\partial x^\mu}+B^2 .
$$

The partial derivatives commute, and the monomials $\partial^2/\partial x^\mu\partial x^\nu$, $\partial/\partial x^\mu$ and $1$ are independent over the constants, so the coefficients of each monomial must agree with those of $(\Box-\lambda)I_n$. The second derivatives give $\gamma_\mu\gamma_\nu+\gamma_\nu\gamma_\mu=2g_{\mu\nu}I_n$; the first derivatives give the anticommutator with $B$; and the constant term gives the square. The converse is the same computation read backwards.

The three conditions separate. The first is the **Clifford condition**; it involves neither $B$ nor $\lambda$. The second says that the zero-order term anticommutes with every generator. The third fixes its square. The shift enters the first-order term only through the anticommutator, and its value only through the square.

**The principal symbol.** The principal symbol of $D$ is $\sum_\mu q_\mu\gamma_\mu$. The Clifford condition says that its square is $(g_{\mu\nu}q_\mu q_\nu)I_n$. The zero-order term and the shift are lower order. A root is therefore a four-generator Clifford system before it is a shifted d'Alembertian; the shift is a condition on the constant term, not on the principal symbol.

**The material sector.** On $\mathbb{M}_-$, where $Q_t=iq'_t$, the same d'Alembertian reads $\Box=\Delta-\partial^2/\partial(q'_t)^2$. The article works in these real coordinates, where the Clifford relation is $2g^{\mu\nu}$ with $g=\mathrm{diag}(+1,-1,-1,-1)$; the $Q$ coordinates carry the Euclidean transcription and are not used for the root.

## The Clifford Algebra and the Minimal Carrier

### The Classification

**Theorem.** Four matrices satisfying $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_n$ generate the complex Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$. Its smallest faithful module is $\mathbb{C}^4$, and no such quadruple exists in $M_n(\mathbb{C})$ with $n<4$.

*Proof.* The monomials

$$
I,\qquad \gamma_\mu,\qquad \gamma_\mu\gamma_\nu\ (\mu<\nu),\qquad
\gamma_\mu\gamma_\nu\gamma_\rho\ (\mu<\nu<\rho),\qquad \gamma_5,
\qquad \gamma_5=i\gamma_t\gamma_x\gamma_y\gamma_z,
$$

are sixteen in number: one identity, four generators, six products of two, four products of three and the volume element. They form a basis of the Clifford algebra, which is simple; a nonzero representation is faithful, so the sixteen matrices are linearly independent. Sixteen independent matrices in $M_n(\mathbb{C})$ require $n^2\ge16$, hence $n\ge4$. The bound is attained by the frame of §*The Four Generators* below.

**Corollary.** The carrier of a root of $\Box-\lambda$ has complex dimension at least four. On $\mathbb{C}^4$ the root is unique up to similarity: any two faithful modules of $M_4(\mathbb{C})$ are isomorphic, and the frames are related by $GL_4(\mathbb{C})$.

### The Three Generators Inside the Algebra

**Proposition.** The elements $\vec e_k$, $k=x,y,z$, satisfy

$$
\vec e_k^2=-e_t,\qquad \{\vec e_j,\vec e_k\}=0\quad(j\ne k).
$$

They generate $\mathbb{B}$ itself, and the left action gives the isomorphism $\mathbb{B}\cong\mathrm{End}_{\mathbb{C}}(S)=M_2(\mathbb{C})$ on the simple module $S=\mathbb{C}^2$. The complex Clifford algebra $\mathrm{Cl}_3(\mathbb{C})$ is $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$; the three generators generate one of the two summands, and that summand is $\mathbb{B}$.

*Proof.* The square is $\vec e_k^2=-e_t$. For $j\ne k$, the product is $\vec e_j\vec e_k$, and the anticommutator is $\{\vec e_j,\vec e_k\}=0$. The three generators and their products span the four-dimensional algebra $\mathbb{B}=\mathrm{End}_{\mathbb{C}}(S)$, which is $M_2(\mathbb{C})$.

**Proposition (no fourth left multiplication).** No element $X\in\mathbb{B}$ anticommutes with all three $\vec e_k$.

*Proof.* Write $X=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. The anticommutator with $\vec e_x$ is

$$
\{X,\vec e_x\}=2a_t\vec e_x-2a_x e_t ,
$$

so $a_t=a_x=0$. The anticommutator with $\vec e_y$ then gives $a_y=0$, and $X=a_z\vec e_z$ commutes with $\vec e_z$, so $a_z=0$. Hence $X=0$.

**Corollary.** The left regular image $L(\mathbb{B})$ has complex dimension four and contains no four-generator Clifford system. The fourth generator of a root is not a left multiplication by an element of $\mathbb{B}$.

*Proof.* The map $L$ is injective because $\mathbb{B}$ has a unit, so its image has complex dimension four and is spanned by $L_{e_t},L_{\vec e_x},L_{\vec e_y},L_{\vec e_z}$. A four-generator Clifford system would generate sixteen independent operators, which a four-dimensional image cannot contain.

**The two-dimensional module fails.** On $S$ the left action of the gradient is a first-order operator, but its square is not $\Box I$. The square of $\tilde\nabla$ is

$$
\tilde\nabla^2=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q
+2\frac{\partial}{\partial Q_t}\sum_{k}\vec e_k\frac{\partial}{\partial Q_k},
$$

so it carries a vector remainder and the spatial part has the opposite sign. The principal-symbol obstruction is the dimension count: four anticommuting $2\times2$ matrices do not exist. The sign is a symptom, not the cause.

## The Regular Module and the Two-Sided Direction

### The Two Minimal Left Ideals

Let $\tilde\Pi_+$ and $\tilde\Pi_-$ be the primitive idempotents of the algebra and let

$$
S_+=\mathbb{B}\tilde\Pi_+,\qquad S_-=\mathbb{B}\tilde\Pi_- .
$$

The algebra is their direct sum as a left module,

$$
\mathbb{B}=S_+\oplus S_-,
$$

and each summand is a copy of the simple module $S=\mathbb{C}^2$. Left multiplication by any element preserves each summand, because $\tilde Q_1(\tilde Q_2\tilde\Pi_\pm)=(\tilde Q_1\tilde Q_2)\tilde\Pi_\pm$. A four-generator Clifford system must therefore use the multiplicity of the two summands: the three left multiplications generate only the three-generator system on each copy, and the fourth generator cannot be a left multiplication by the proposition above. The multiplicity is realised by two two-sided operators, the exchange $R_u$ and the grading $G$ below.

### The Swap and the Grading

The standard pair is fixed once for the article:

$$
\tilde\Pi_\pm=\tfrac12\left(e_t\pm i\vec e_z\right),
\qquad
\vec\Upsilon_{+-}=\vec\Upsilon_x=\tfrac12\left(i\vec e_x-\vec e_y\right),
\qquad
\vec\Upsilon_{-+}=\vec\Upsilon_y=\tfrac12\left(i\vec e_x+\vec e_y\right),
$$

so that $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$. The mixed Peirce units obey

$$
\tilde\Pi_+\vec\Upsilon_{+-}=\vec\Upsilon_{+-},\qquad
\vec\Upsilon_{+-}\tilde\Pi_-=\vec\Upsilon_{+-},
$$

$$
\tilde\Pi_-\vec\Upsilon_{-+}=\vec\Upsilon_{-+},\qquad
\vec\Upsilon_{-+}\tilde\Pi_+=\vec\Upsilon_{-+},
$$

$$
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+,\qquad
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_- .
$$

Put

$$
u=\vec\Upsilon_{+-}+\vec\Upsilon_{-+}=i\vec e_x .
$$

**Proposition.** The element $u$ satisfies $u^2=e_t$, and the right multiplication $R_u$ is an involution that exchanges $S_+$ and $S_-$. In the adapted bases $(\tilde\Pi_+,\vec\Upsilon_{-+})$ of $S_+$ and $(\vec\Upsilon_{+-},\tilde\Pi_-)$ of $S_-$, it is the identity across the two summands.

*Proof.* The square is $u^2=\vec\Upsilon_{+-}^2+\vec\Upsilon_{-+}^2+\vec\Upsilon_{+-}\vec\Upsilon_{-+}+\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_++\tilde\Pi_-=e_t$, the mixed squares vanishing. For $\tilde Q_1=a\tilde\Pi_++c\vec\Upsilon_{-+}\in S_+$,

$$
\tilde Q_1u=a\tilde\Pi_+u+c\vec\Upsilon_{-+}u
=a\vec\Upsilon_{+-}+c\tilde\Pi_- \in S_- ,
$$

and for $\eta=b\vec\Upsilon_{+-}+d\tilde\Pi_-\in S_-$,

$$
\eta u=b\vec\Upsilon_{+-}u+d\tilde\Pi_-u
=b\tilde\Pi_++d\vec\Upsilon_{-+}\in S_+ .
$$

The coordinates $(a,c)$ and $(b,d)$ are preserved, so $R_u$ is the identity across the summands in the adapted bases, and applying it twice returns the original element.

**Proposition.** Let $G=R_{\tilde\Pi_+}-R_{\tilde\Pi_-}$. Then $G^2=I$, $G$ acts as $+1$ on $S_+$ and as $-1$ on $S_-$, and $R_uG=-GR_u$.

*Proof.* Since $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$,

$$
G^2=R_{(\tilde\Pi_+-\tilde\Pi_-)^2}=R_{\tilde\Pi_++\tilde\Pi_-}=I .
$$

For $\tilde Q_1\in S_+$, $\tilde Q_1\tilde\Pi_+=\tilde Q_1$ and $\tilde Q_1\tilde\Pi_-=0$, so $G\tilde Q_1=\tilde Q_1$; for $\tilde Q_2\in S_-$, $G\tilde Q_2=-\tilde Q_2$. The exchange gives $\tilde\Pi_+u=\vec\Upsilon_{+-}=u\tilde\Pi_-$ and $\tilde\Pi_-u=\vec\Upsilon_{-+}=u\tilde\Pi_+$. Using $R_aR_b=R_{ba}$,

$$
R_uG=R_{\tilde\Pi_+u}-R_{\tilde\Pi_-u}
=R_{u\tilde\Pi_-}-R_{u\tilde\Pi_+}=-GR_u .
$$

### The Four Generators

Define

$$
\gamma_t=R_u,\qquad
\gamma_k=L_{\vec e_k}G\quad(k=x,y,z).
$$

**Theorem.** The four operators $\gamma_t,\gamma_x,\gamma_y,\gamma_z$ satisfy

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I,
$$

they are two-sided operators, and they generate $M_4(\mathbb{C})$. The cell root acts on the regular module $\mathbb{B}$.

*Proof.* The square of $\gamma_t$ is $R_u^2=R_{u^2}=I$. The square of $\gamma_k$ is $L_{\vec e_k}^2G^2=-I$, because $\vec e_k^2=-e_t$ and $G^2=I$. For $j\ne k$,

$$
\{\gamma_j,\gamma_k\}
=L_{\vec e_j\vec e_k+\vec e_k\vec e_j}G^2=0 .
$$

The mixed anticommutator is

$$
\gamma_t\gamma_k+\gamma_k\gamma_t
=R_uL_{\vec e_k}G+L_{\vec e_k}GR_u
=L_{\vec e_k}(R_uG+GR_u)=0,
$$

because left and right multiplications commute and $R_uG=-GR_u$. Hence the Clifford relations hold. The operators are two-sided:

$$
\gamma_t=T_{e_t,u},\qquad
\gamma_k=T_{\vec e_k,\tilde\Pi_+}-T_{\vec e_k,\tilde\Pi_-},
$$

so they lie in the enveloping algebra $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$. The sixteen monomials are independent by the Clifford relations, so they generate the whole of $M_4(\mathbb{C})$.

**The cells.** With $T_{a,b}=L_aR_b$, the same frame is a set of cells of the two-sided algebra. The volume element of the frame is

$$
\gamma_5=i\gamma_t\gamma_x\gamma_y\gamma_z=iT_{e_t,e_y},
$$

and the split of each operator between the two sides is

| $T$ | $L$ | $R$ |
|---|---|---|
| $\gamma_t=T_{e_t,u}$ | $L_{e_t}=I$ | $R_u$ |
| $\gamma_k=T_{\vec e_k,\tilde\Pi_+}-T_{\vec e_k,\tilde\Pi_-}$ | $L_{\vec e_k}$ | $R_{\tilde\Pi_+}-R_{\tilde\Pi_-}=G$ |
| $\gamma_5=iT_{e_t,e_y}$ | $L_{e_t}=I$ | $iR_{e_y}$ |

The fourth generator is the cell $T_{e_t,u}$, a pure right multiplication: its left factor is the identity, and it lies in the commutant of the left copy.

**The matrix frame.** In the adapted basis of the two summands,

$$
\gamma_t=\sigma_1\otimes I_2,\qquad
\gamma_k=\sigma_3\otimes\vec e_k,\qquad
\gamma_5=i\gamma_t\gamma_x\gamma_y\gamma_z=-\sigma_2\otimes I_2 .
$$

Each generator squares to $\pm I$, with $\gamma_t$ positive and the three spatial generators negative; distinct generators anticommute, and $\gamma_5$ anticommutes with all four and squares to the identity. The matrices $\sigma_1,\sigma_2,\sigma_3$ act on the multiplicity factor, and the elements $\vec e_k$ act on the simple module $S$.

**Remark (why the grading).** The exchange $R_u$ commutes with every left multiplication, so it cannot anticommute with $L_{\vec e_k}$. The grading turns the commutation into an anticommutation, which is why the spatial generators are $L_{\vec e_k}G$ and not $L_{\vec e_k}$. This is the precise sense in which the fourth direction is two-sided: the three spatial generators use both sides, and the fourth is the exchange.

**Remark (the chiral halves are not the ideals).** The eigenspaces of $\gamma_5$ are two-dimensional and mix $S_+$ and $S_-$; they are not left ideals. The minimal left ideals are the two copies of $S$, and the chiral projectors of $\gamma_5$ are a different split. The distinction is the one of *The Two Chiralities of $M_4(\mathbb{C})$*, read on the regular module.

## The Unshifted Cell Root

**Theorem.** Let

$$
\mathsf D=i\sum_{\mu\in\{t,x,y,z\}}\gamma_\mu\frac{\partial}{\partial x^\mu}.
$$

Then $\mathsf D^2=\Box I_4$.

*Proof.* The Clifford relation gives

$$
\mathsf D^2=-\frac12\sum_{\mu,\nu}\{\gamma_\mu,\gamma_\nu\}
\frac{\partial^2}{\partial x^\mu\partial x^\nu}
=-g^{\mu\nu}\frac{\partial^2}{\partial x^\mu\partial x^\nu}I_4
=\Box I_4 .
$$

The operator $\mathsf D$ is a two-sided differential operator: each $\gamma_\mu$ is a two-sided constant operator, so $\mathsf D$ is a sum of terms $T_{a,b}\partial_\mu$. It acts on $\mathbb{B}$-valued fields, and its square is the scalar d'Alembertian. It is not left multiplication by an element of $\mathbb{B}$: the timelike generator is the exchange $R_u$, and the spatial generators are left multiplications corrected by the grading. Its coefficients are cells of $\mathbb{B}^{\mathrm e}$, and the gradient $\tilde\nabla$ is the element of $\mathbb{B}$ that supplies the factorisation $\tilde\nabla\tilde\nabla^{\natural}=\Box$.

**The kernel at $\lambda=0$.** The equation $\mathsf D\psi=0$ is the unshifted cell root. In the chiral frame of §*The Chiral Form* it decouples into $D_-\psi_-=0$ and $D_+\psi_+=0$; its kernel is a chiral half of the full solution space of $\Box\psi=0$.

**Non-uniqueness.** The cell root is unique up to similarity, not canonical. A formula that names a particular $\gamma$-frame is therefore frame data; the invariant statement is the factorisation in $\mathbb{B}$. The canonical frame fixes the Peirce basis, and the root still depends on the exchange $u$; the biquaternion structure gives a canonical decomposition into the two minimal left ideals, but not a canonical root. The sign of $\gamma_5$ and the exchange of $c$ with $-c$ give the same operator up to a change of frame.

## The Shifted D'Alembertian

### The Single Square

**Theorem.** Let $\lambda\in\mathbb{C}$ and let $c\in\mathbb{C}$ satisfy $c^2=-\lambda$. Then

$$
\mathsf D_\lambda=\mathsf D+c\gamma_5
$$

satisfies

$$
\mathsf D_\lambda^2=(\Box-\lambda)I_4 .
$$

*Proof.* Every generator anticommutes with $\gamma_5$, so $\mathsf D\gamma_5+\gamma_5\mathsf D=0$. Since $\gamma_5^2=I$,

$$
\mathsf D_\lambda^2=\mathsf D^2+c(\mathsf D\gamma_5+\gamma_5\mathsf D)+c^2\gamma_5^2
=\Box I_4+c^2I_4=(\Box-\lambda)I_4 .
$$

**Theorem (the converse).** Every constant-coefficient root of $\Box-\lambda$ with principal symbol $\sum_\mu q_\mu\gamma_\mu$ is of the form $\mathsf D_\lambda=\mathsf D+c\gamma_5$ with $c^2=-\lambda$, up to similarity.

*Proof.* By the root condition, $B$ anticommutes with every $\gamma_\mu$. Then $B\gamma_5$ commutes with every $\gamma_\mu$, hence with the algebra they generate, which is $M_4(\mathbb{C})$. The commutant of $M_4(\mathbb{C})$ is the scalars, so $B\gamma_5=cI$ and $B=c\gamma_5$. The condition $B^2=-\lambda I$ gives $c^2=-\lambda$.

**The type of the shift.** The zero-order term is necessarily a multiple of the volume element; it cannot be a central scalar unless $\lambda=0$. Over $\mathbb{C}$ every $\lambda$ has a root $c$, and the two roots are opposite. If $\lambda$ is real and positive, $c$ is imaginary; if $\lambda$ is real and negative, $c$ is real. The two signs of $c$ give the two roots $\mathsf D\pm c\gamma_5$; the algebra prefers neither.

### The Scalar Shift

**Theorem.** For every $\kappa\in\mathbb{C}$,

$$
(\mathsf D-\kappa I)(\mathsf D+\kappa I)=\Box-\kappa^2 .
$$

No single operator $\mathsf D+\kappa I$ squares to $\Box-\kappa^2$ for $\kappa\ne0$.

*Proof.* The product is $\mathsf D^2-\kappa^2I$ because $\mathsf D$ commutes with the scalar $\kappa I$. For the second statement, the cross term of $(\mathsf D+\kappa I)^2$ is $2\kappa\mathsf D$, which does not vanish for $\kappa\ne0$; equivalently, $\{\kappa I,\gamma_\mu\}=2\kappa\gamma_\mu\ne0$, so the anticommutator condition fails.

At $\lambda=0$, $\kappa=0$, and the two pictures coincide: $\mathsf D^2=\Box$. The scalar factorisation is a product of two first-order factors whose product is the shifted d'Alembertian; each factor alone is not a root. The single square is one first-order operator whose zero-order term anticommutes with the generators; it is a root, but its zero-order term is pseudoscalar.

### The Chiral Form

The volume element defines the chiral projectors

$$
P_+=\frac12(I+\gamma_5),\qquad P_-=\frac12(I-\gamma_5),
\qquad P_++P_-=I,\quad P_\pm^2=P_\pm .
$$

Because $\mathsf D$ anticommutes with $\gamma_5$, it exchanges the two chiral halves. In the chiral basis, where $\gamma_5=\operatorname{diag}(I_2,-I_2)$, write

$$
\mathsf D=\begin{pmatrix}0&D_-\\ D_+&0\end{pmatrix},
\qquad
D_-D_+=D_+D_-=\Box I_2 .
$$

The last identity is the chiral block form of $\mathsf D^2=\Box I_4$. The cell root is

$$
\mathsf D_\lambda=\begin{pmatrix}cI_2&D_-\\ D_+&-cI_2\end{pmatrix}.
$$

**The two rows.** Write $\psi=(\psi_+,\psi_-)$ in the chiral decomposition. The equation $\mathsf D_\lambda\psi=0$ is the pair

$$
D_-\psi_-=-c\psi_+,\qquad
D_+\psi_+=c\psi_- .
$$

For $c\ne0$, the second row determines $\psi_-$ from $\psi_+$,

$$
\psi_-=\frac1cD_+\psi_+ ,
$$

and the first row is then equivalent to

$$
(\Box-\lambda)\psi_+=0 ,
$$

because $D_-\psi_-=\frac1cD_-D_+\psi_+=\frac1c\Box\psi_+$ and $\lambda=-c^2$. The projection $\psi\mapsto\psi_+$ is an isomorphism from $\ker \mathsf D_\lambda$ onto the solution space of the shifted d'Alembertian on one chiral component; the other component is determined. The kernel of the single root is therefore a **chiral half** of the full four-component solution space. At $c=0$ the two rows decouple, $D_-\psi_-=0$ and $D_+\psi_+=0$, and the kernel is still a half.

**The factorisation kernel.** For $\kappa\ne0$, on the solution space of $(\Box-\kappa^2)\psi=0$, define

$$
Q_+=\frac{1}{2\kappa}(\kappa I+\mathsf D),\qquad
Q_-=\frac{1}{2\kappa}(\kappa I-\mathsf D).
$$

Then $Q_++Q_-=I$, $Q_\pm^2=Q_\pm$, and

$$
(\mathsf D-\kappa I)Q_+=0,\qquad
(\mathsf D+\kappa I)Q_-=0 .
$$

The solution space of the shifted d'Alembertian is the direct sum

$$
\ker(\Box-\kappa^2)=\ker(\mathsf D-\kappa I)\oplus\ker(\mathsf D+\kappa I),
$$

and the two factors together capture the whole second-order kernel. These projectors are the spectral projectors of $\mathsf D$ on the shell; they are not the chiral projectors. The single root captures one chiral half, while the scalar factorisation captures the full space as the sum of its two first-order halves. At $\kappa=0$ the projectors are undefined, the two factors coincide, and the kernel of $\Box$ is strictly larger than the kernel of $\mathsf D$.

**The characteristic variety.** The symbol of $\mathsf D_\lambda$ is $\sum_\mu q_\mu\gamma_\mu+c\gamma_5$. Its determinant is $(g_{\mu\nu}q_\mu q_\nu-\lambda)^2$, so the first-order operator is singular exactly on the quadric $g_{\mu\nu}q_\mu q_\nu=\lambda$. On that quadric the symbol of $\mathsf D_\lambda$ has a two-dimensional kernel, while the symbol of $\Box-\lambda$ has a four-dimensional kernel; the factor of two is the chiral half.

### The Determinant

In the chiral frame the determinant of the block matrix is

$$
\det \mathsf D_\lambda
=\det(cI_2)\det\Bigl(-cI_2-\frac1cD_+D_-\Bigr)
=c^2\Bigl(-c-\frac{\Box}{c}\Bigr)^2
=(\Box-\lambda)^2 .
$$

At $\lambda=0$ this is $\det\mathsf D=\Box^2$. The same expression is the determinant of the left regular matrix of the gradient,

$$
\det\mathsf M_4^{L}(\tilde\nabla)=\langle\tilde\nabla\rangle_{\natural}^2=\Box^2 ,
$$

read on the symbol, because the determinant of the left regular matrix of an element is the square of its quaternionic norm (*$M_4(\mathbb{C})_{\mathbb{B}}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*). The agreement is a consistency check, not a construction: the determinant sees the square of the shifted d'Alembertian, while the kernel of the single root is a chiral half. A determinant identity is not a square root.

## The Classification of Carriers

The table classifies the carriers on which the constant-coefficient Clifford ansatz of this article can be solved. The **carrier** is the complex vector space on which the root acts; the **Clifford system** is the number of anticommuting generators available on it. The central scalar is the one-dimensional carrier $\mathbb{C}e_t$; the simple module is $S=\mathbb{B}\tilde\Pi$, of complex dimension two; the regular module is $\mathbb{B}=S_+\oplus S_-$, of complex dimension four.

| carrier | complex dimension | Clifford system | root of $\Box$ | single root of $\Box-\lambda$, $\lambda\ne0$ | scalar factorisation |
|---|---|---|---|---|---|
| $\mathbb{C}e_t$ | $1$ | none | no | no | no |
| $S=\mathbb{B}\tilde\Pi$ | $2$ | three generators | no | no | no |
| $\mathbb{B}=S_+\oplus S_-$ | $4$ | four generators | yes | yes, pseudoscalar shift | yes, scalar shift |
| $\mathbb{B}^{\oplus m}$, $m>1$ | $4m$ | four generators | yes | yes | yes, not minimal |

**The minimal carrier.** The regular module is minimal. Any larger carrier is a direct sum of copies of it, and the cell root acts componentwise; the Clifford system has the same four generators, and the root is not new. The simple module carries the three-generator system generated by the three $\vec e_k$, but no four-generator system, by the dimension count. The central scalar carries none.

**The scope.** The table is a classification of the carriers of the Clifford ansatz, not a classification of all first-order operators whose square is scalar. A first-order operator with a non-Clifford principal symbol is outside the article.

## The Freedom of the Frame

The Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})$ has a unique irreducible module up to isomorphism, so any two frames of the root are related by an invertible matrix:

$$
\gamma_{\mu}'=S\gamma_\mu S^{-1},\qquad B'=SBS^{-1},\qquad S\in GL_4(\mathbb{C}).
$$

The biquaternion structure does not select a canonical matrix frame. It selects the decomposition $\mathbb{B}=S_+\oplus S_-$, the exchange $u=i\vec e_x$, and the grading $G=R_{i\vec e_z}$; the adapted basis and the identification of the two summands with $S$ are choices. The physics twin, *The First-Order Root of the Biquaternion Klein–Gordon Operator*, writes another frame of the same algebra, $\gamma_0=iT_{e_t,e_x}=iR_x$, $\gamma_k=iT_{e_k,e_y}$, $\gamma_5=-iT_{e_t,e_z}$, related to the frame above by a similarity. The volume element is canonical up to the sign of the orientation of the four generators, and the two signs of $c$ give the same operator up to the exchange $\gamma_5\mapsto-\gamma_5$. The root is unique up to similarity, not canonical.

**The two signs.** The sign of $c$ selects one of the two opposite roots. The sign of $\gamma_5$ is the orientation of the four generators, and it changes the chiral decomposition and the pair of rows. Neither sign changes the operator identity $\mathsf D_\lambda^2=(\Box-\lambda)I$.

## Worked Examples

**A plane wave.** Let $\psi(x)=\exp(-i\sum_\mu q_\mu x^\mu)v$ with $v\in\mathbb{C}^4$ constant and $q_\mu\in\mathbb{C}$. Then

$$
\mathsf D\psi=\Bigl(\sum_\mu q_\mu\gamma_\mu\Bigr)\psi,
\qquad
\mathsf D_\lambda\psi=\Bigl(\sum_\mu q_\mu\gamma_\mu+c\gamma_5\Bigr)\psi .
$$

The first-order equation has a nonzero solution exactly when the determinant vanishes, that is on the quadric $g^{\mu\nu}q_\mu q_\nu=\lambda$. On the quadric the symbol has a two-dimensional kernel.

**The unshifted cell root on a constant spinor.** A constant $v\in\mathbb{C}^4$ satisfies $\mathsf D v=0$ and $\Box v=0$. The example shows that the cell root has a nontrivial kernel already at $\lambda=0$. The constant solutions of $\Box$ are all of $\mathbb{C}^4$, and $\mathsf D$ vanishes on all of them, so the constant part of the kernel does not distinguish the chiral halves; the half appears on the non-constant solutions of §*The Chiral Form*.

**Promotion of a chiral solution.** Let $\psi_+$ solve $(\Box-\lambda)\psi_+=0$ with $c\ne0$, and put $\psi_-=\frac1cD_+\psi_+$. Then

$$
D_+\psi_+=c\psi_-,\qquad
D_-\psi_-=\frac1cD_-D_+\psi_+=\frac1c\Box\psi_+=-c\psi_+,
$$

so $\mathsf D_\lambda(\psi_+,\psi_-)=0$. The example exhibits the isomorphism between the kernel of the single root and the chiral half of the shifted d'Alembertian.

**The scalar factorisation.** Let $\kappa\ne0$ and let $v$ satisfy $(\sum_\mu q_\mu\gamma_\mu-\kappa I)v=0$ for a covector $q$ with $g_{\mu\nu}q_\mu q_\nu=\kappa^2$. Then $(\mathsf D-\kappa I)\psi=0$ for the corresponding plane wave, and the product $(\mathsf D+\kappa I)(\mathsf D-\kappa I)\psi=0$. The other factor is obtained by $\kappa\mapsto-\kappa$. The example shows the two halves of the factorisation.

**The determinant at $\lambda=0$.** For the constant-coefficient operator $\mathsf D$, the determinant of the symbol is

$$
\det\Bigl(\sum_\mu q_\mu\gamma_\mu\Bigr)
=\Bigl(g^{\mu\nu}q_\mu q_\nu\Bigr)^2 ,
$$

the square of the symbol of $\Box$, the same expression as the determinant of the left regular matrix of the gradient. At $\lambda\ne0$ the determinant is $\bigl(g^{\mu\nu}q_\mu q_\nu-\lambda\bigr)^2$.

## Summary

The d'Alembertian $\Box=\partial^2/\partial Q_t^2+\Delta_Q=-g_{\mu\nu}\partial_\mu\partial_\nu$ is the quaternionic norm of the gradient and a scalar second-order operator. The algebra itself is $M_2(\mathbb{C})$; the four-dimensional carrier is its regular module, and the $M_4(\mathbb{C})$ of the root is the operator algebra on that module, not a second representation of $\mathbb{B}$. It has no Clifford root on the two-dimensional simple module of $\mathbb{B}$: the three generators $\vec e_k$ supply a three-generator Clifford system, and no fourth element of the algebra anticommutes with all three. The minimal carrier is the four-dimensional regular module $\mathbb{B}=S_+\oplus S_-$; the fourth generator is the two-sided exchange of the two minimal left ideals, and the three spatial generators are the left multiplications corrected by the grading. The unshifted cell root is $\mathsf D=i\sum_\mu\gamma_\mu\partial_\mu$, with $\mathsf D^2=\Box I$; its coefficients lie in the enveloping algebra $\mathbb{B}^{\mathrm e}$, not in $\mathbb{B}$, and the biquaternion object is the factorisation of the unshifted operator, $\tilde\nabla\tilde\nabla^{\natural}=\Box$. The shifted operator $\Box-\lambda$ has a single root exactly when the zero-order term is the pseudoscalar $c\gamma_5$ with $c^2=-\lambda$; a scalar shift admits only the factorisation $(\mathsf D-\kappa)(\mathsf D+\kappa)=\Box-\kappa^2$. The single root has a chiral half as its kernel; for $\kappa\ne0$, the scalar factorisation captures the full second-order kernel as the sum of its two first-order factors. The determinant of the single root is $(\Box-\lambda)^2$, the same expression as the determinant of the left regular matrix of the gradient at $\lambda=0$. The cell root is unique up to similarity, not canonical; the biquaternion structure supplies the decomposition and the exchange, not a preferred matrix frame, and a formula naming a particular frame is frame data.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | the biquaternionic gradient |
| $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial Q_\mu$ | its quaternion conjugate, $\varepsilon=(1,-1,-1,-1)$ |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$ | the d'Alembertian $\partial^2/\partial Q_t^2+\Delta_Q=-g^{\mu\nu}\partial_\mu\partial_\nu$ |
| $x^\mu=(q'_t,x,y,z)$ | the real coordinates, $Q_t=iq'_t$ |
| $g_{\mu\nu}$ | the metric $\mathrm{diag}(+1,-1,-1,-1)$ |
| $q_\mu$ | the complex symbol variable dual to $i\partial_\mu$ |
| $\vec e_k$ | the three generators inside $\mathbb{B}$, $\vec e_k^2=-e_t$ |
| $\gamma_\mu$ | the four generators of the root on the regular module |
| $\gamma_5=i\gamma_t\gamma_x\gamma_y\gamma_z$ | the volume element, $\gamma_5^2=I$ |
| $T_{a,b}=L_aR_b$ | the two-sided cell, acting by $\tilde Q\mapsto a\tilde Qb$ |
| $\gamma_t=T_{e_t,u}$, $\gamma_k=T_{\vec e_k,\tilde\Pi_+}-T_{\vec e_k,\tilde\Pi_-}$, $\gamma_5=iT_{e_t,e_y}$ | the frame as cells of $T$ |
| $\mathsf D=i\sum_\mu\gamma_\mu\partial_\mu$ | the unshifted **cell** root in $\mathbb{B}^{\mathrm e}$, $\mathsf D^2=\Box I$; not an element of $\mathbb{B}$ |
| $\mathsf D_\lambda=\mathsf D+c\gamma_5$, $c^2=-\lambda$ | the single root of $\Box-\lambda$ |
| $\kappa$, $(\mathsf D-\kappa)(\mathsf D+\kappa)$ | the scalar shift and its factorisation |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two minimal left ideals, the two copies of the simple module |
| $u=\vec\Upsilon_{+-}+\vec\Upsilon_{-+}=i\vec e_x$ | the exchange, $u^2=e_t$, $R_u=R_{i\vec e_x}$ |
| $R_u$, $G=R_{\tilde\Pi_+}-R_{\tilde\Pi_-}=R_{i\vec e_z}$ | the exchange operator and the grading |
| $P_\pm=\frac12(I\pm\gamma_5)$ | the chiral projectors |
| $Q_\pm=\frac{1}{2\kappa}(\kappa I\pm\mathsf D)$ | the spectral projectors of the scalar factorisation, $\kappa\ne0$ |

## Further Reading

- [Conventions in Mathematics](conventions-in-mathematics.html), for the derivative conventions and the gradient.
- [The $M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the target representation of the algebra.
- [Biquaternion Analysis](biquaternion-analysis.html), for the gradient, its conjugate and the d'Alembertian at length.
- [Conventions of the Operators and the Differential Calculus](conventions-of-the-operators-and-the-differential-calculus.html), for the four forms, the four norms and the definition of the d'Alembertian.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the two summands of the regular module.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the Peirce bases, the mixed units and the exchange.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the operators $T_{\tilde Q_1,\tilde Q_2}$ and their composition.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$ and the spanning theorem.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the gamma set, the volume element and its place among the sixteen cells.
- [Bott Periodicity and the Classification](bott-periodicity-and-the-classification.html), for $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$ and the minimal module.
- [Operators on a Clifford Module](operators-on-a-clifford-module.html), for the Clifford action and the symbol.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chiral split and the distinction from the minimal left ideals.
