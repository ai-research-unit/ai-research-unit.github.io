# __The First-Order Root of the Biquaternion D'Alembertian__

## Introduction

The d'Alembertian of the biquaternion algebra is the scalar second-order operator

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla\bigr)
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q ,
$$

the quaternionic norm of the gradient. This article asks for a first-order operator $D$ whose square is $\Box$, or the shifted operator $\Box-\lambda$ for a complex number $\lambda$.

The question has two answers, and they are different. A **single square** is one first-order operator $D$ with $D^2=(\Box-\lambda)I$. A **factorisation** is a product $D_-D_+=(\Box-\lambda)I$ of two first-order operators. The single square is the stronger equation: its kernel is a chiral half of the second-order solution space. The factorisation is the weaker pair: when the two factors are distinct, the two first-order equations together are equivalent to the second-order equation. At $\lambda=0$ the two coincide at the level of the operator, but the kernel of the root is still a half.

**The results.** The d'Alembertian has no first-order root on the two-dimensional simple module of $\mathbb{B}$. The minimal carrier is four-dimensional, the regular module $\mathbb{B}\cong S_+\oplus S_-$. The three elements $i\vec e_k$ supply a rank-three Clifford system inside the algebra; the fourth generator is not a left multiplication by an element of $\mathbb{B}$, but the two-sided direction that exchanges the two minimal left ideals. On the regular module the unshifted root is $\mathsf D=\sum_\mu\Gamma^\mu\partial/\partial Q_\mu$, with $\mathsf D^2=\Box I$. The shifted operator has a single root exactly when the zero-order term is a pseudoscalar $c\Gamma_5$ with $c^2=-\lambda$; a scalar shift admits only the factorisation $(\mathsf D-\kappa)(\mathsf D+\kappa)$.

The article is mathematics. The d'Alembertian is the norm of the gradient, and no physical interpretation is used. The conventions are those of *Conventions in Mathematics* and *The Differential Operators, the Products, the Forms and the D'Alembertian*; the two-sided operators are *Two-Sided Operators on the Biquaternion Algebra* and *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the minimal left ideals are *The Minimal Left Ideals* and *Spinors as Peirce Coordinates in the Biquaternion Algebra*.

## The D'Alembertian and Its Symbol

### The Algebra and the Gradient

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, where $e_t=1$ is the scalar unit and the three vector units satisfy $\vec e_k^2=-e_t$ and the quaternion relations. A general element is

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu ,
$$

with complex coefficients $Q_\mu=q_\mu+iq'_\mu$. The coordinate derivative is written $\partial/\partial Q_\mu$, and the derivative along the fourth coordinate is $\partial/\partial Q_t$; on the material sector, where $Q_t=iq'_t$, it reads $\partial/\partial Q_t=-i\,\partial/\partial q'_t$. The biquaternionic gradient is

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

**The d'Alembertian is not the partner operator.** The plain bilinear norm of the gradient is $\partial^2/\partial Q_t^2-\Delta_Q$, a different operator, and it has a different root. This article treats $\Box$ only. The two operators are distinguished in *The Differential Operators, the Products, the Forms and the D'Alembertian*, and the distinction is fixed by the form, not by a choice of sign.

### The Symbol

For a constant-coefficient operator, the **symbol** is the matrix polynomial obtained by replacing each derivative $\partial/\partial Q_\mu$ by a complex variable $K_\mu$. The symbol of $\Box$ is

$$
\sigma(\Box)(K)=\sum_{\mu\in\{t,x,y,z\}}K_\mu^2 ,
$$

and the symbol of a first-order operator

$$
D=\sum_{\mu\in\{t,x,y,z\}}\Gamma^\mu\frac{\partial}{\partial Q_\mu}+B,
\qquad \Gamma^\mu,B\in M_n(\mathbb{C})\ \text{constant},
$$

is

$$
\sigma(D)(K)=\sum_{\mu\in\{t,x,y,z\}}K_\mu\Gamma^\mu+B .
$$

For constant coefficients the symbol of a composition is the product of the symbols, so $\sigma(D^2)(K)=\sigma(D)(K)^2$. The operator identity $D^2=(\Box-\lambda)I_n$ is therefore equivalent to the matrix identity

$$
\Bigl(\sum_\mu K_\mu\Gamma^\mu+B\Bigr)^2
=\Bigl(\sum_\mu K_\mu^2-\lambda\Bigr)I_n
$$

for every $K\in\mathbb{C}^4$.

**Proposition (the root condition).** Let $D=\sum_\mu\Gamma^\mu\partial/\partial Q_\mu+B$ with constant $\Gamma^\mu,B\in M_n(\mathbb{C})$. Then $D^2=(\Box-\lambda)I_n$ if and only if

$$
\boxed{\;\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}I_n,\qquad
\{\Gamma^\mu,B\}=0\quad\text{for every }\mu,\qquad
B^2=-\lambda I_n.\;}
$$

*Proof.* Expanding the square gives

$$
D^2=\frac12\sum_{\mu,\nu}\{\Gamma^\mu,\Gamma^\nu\}\frac{\partial^2}{\partial Q_\mu\partial Q_\nu}
+\sum_\mu\{\Gamma^\mu,B\}\frac{\partial}{\partial Q_\mu}+B^2 .
$$

The partial derivatives commute, and the monomials $\partial^2/\partial Q_\mu^2$, $\partial^2/\partial Q_\mu\partial Q_\nu$ with $\mu<\nu$, $\partial/\partial Q_\mu$ and $1$ are independent over the constants, so the coefficients of each monomial must agree with those of $(\Box-\lambda)I_n$. The diagonal second derivatives give $\Gamma^\mu\Gamma^\mu=I_n$; the mixed ones give $\Gamma^\mu\Gamma^\nu+\Gamma^\nu\Gamma^\mu=0$; the first derivatives give the anticommutator with $B$; and the constant term gives the square. The converse is the same computation read backwards.

The three conditions separate. The first is the **Clifford condition**; it involves neither $B$ nor $\lambda$. The second says that the zero-order term anticommutes with every generator. The third fixes its square. The shift enters the first-order term only through the anticommutator, and its value only through the square.

**The principal symbol.** The principal symbol of $D$ is $\sum_\mu K_\mu\Gamma^\mu$. The Clifford condition says that its square is $(\sum_\mu K_\mu^2)I_n$. The zero-order term and the shift are lower order. A root is therefore a rank-four Clifford system before it is a shifted d'Alembertian; the shift is a condition on the constant term, not on the principal symbol.

**The material sector.** On $\mathbb{M}_-$, where $Q_t=iq'_t$, the same d'Alembertian reads $\Box=\Delta-\partial^2/\partial(q'_t)^2$. The Clifford relation in the real coordinates is obtained by multiplying the fourth generator by $i$; the article stays in the $Q$ coordinates, where the relation is all-plus.

## The Clifford Algebra and the Minimal Carrier

### The Classification

**Theorem.** Four matrices satisfying $\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}I_n$ generate the complex Clifford algebra $\mathbb{C}\mathrm{l}_4\cong M_4(\mathbb{C})$. Its smallest faithful module is $\mathbb{C}^4$, and no such quadruple exists in $M_n(\mathbb{C})$ with $n<4$.

*Proof.* The monomials

$$
I,\qquad \Gamma^\mu,\qquad \Gamma^\mu\Gamma^\nu\ (\mu<\nu),\qquad
\Gamma^\mu\Gamma_5,\qquad \Gamma_5,
\qquad \Gamma_5=\Gamma^t\Gamma^x\Gamma^y\Gamma^z,
$$

are sixteen in number: one identity, four generators, six products of two, four products of three and the volume element. They form a basis of the Clifford algebra, which is simple; a nonzero representation is faithful, so the sixteen matrices are linearly independent. Sixteen independent matrices in $M_n(\mathbb{C})$ require $n^2\ge16$, hence $n\ge4$. The bound is attained by the frame of §*The Four Generators* below.

**Corollary.** The carrier of a root of $\Box-\lambda$ has complex dimension at least four. On $\mathbb{C}^4$ the root is unique up to similarity: any two faithful modules of $M_4(\mathbb{C})$ are isomorphic, and the frames are related by $GL_4(\mathbb{C})$.

### The Three Generators Inside the Algebra

**Proposition.** The elements $\gamma_k=i\vec e_k$, $k=x,y,z$, satisfy

$$
\gamma_k^2=e_t,\qquad \{\gamma_j,\gamma_k\}=0\quad(j\ne k).
$$

They generate the full matrix algebra $\mathrm{End}_{\mathbb{C}}(S)=M_2(\mathbb{C})$ in the left action on the simple module $S=\mathbb{C}^2$. The abstract Clifford algebra $\mathbb{C}\mathrm{l}_3$ is $M_2(\mathbb{C})\times M_2(\mathbb{C})$, and the left action selects one of the two components.

*Proof.* The square is $\gamma_k^2=i^2\vec e_k^2=(-e_t)(-e_t)=e_t$. For $j\ne k$, the product is $\gamma_j\gamma_k=i^2\vec e_j\vec e_k=-\vec e_j\vec e_k$, and the anticommutator is $-\{\vec e_j,\vec e_k\}=0$. The three generators and their products span the four-dimensional algebra $\mathbb{B}=\mathrm{End}_{\mathbb{C}}(S)$, which is $M_2(\mathbb{C})$.

**Proposition (no fourth left multiplication).** No element $X\in\mathbb{B}$ anticommutes with all three $\gamma_k$.

*Proof.* Write $X=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. Anticommuting with $\gamma_x=i\vec e_x$ is equivalent to anticommuting with $\vec e_x$, since $i$ is central and nonzero. The anticommutator with $\vec e_x$ is

$$
\{X,\vec e_x\}=2a_t\vec e_x-2a_x e_t ,
$$

so $a_t=a_x=0$. The anticommutator with $\vec e_y$ then gives $a_y=0$, and $X=a_z\vec e_z$ commutes with $\vec e_z$, so $a_z=0$. Hence $X=0$.

**Corollary.** The left regular image $L(\mathbb{B})$ has complex dimension four and contains no rank-four Clifford system. The fourth generator of a root is not a left multiplication by an element of $\mathbb{B}$.

*Proof.* The map $L$ is injective because $\mathbb{B}$ has a unit, so its image has complex dimension four and is spanned by $L_{e_t},L_{\gamma_x},L_{\gamma_y},L_{\gamma_z}$. A rank-four Clifford system would generate sixteen independent operators, which a four-dimensional image cannot contain.

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

and each summand is a copy of the simple module $S=\mathbb{C}^2$. Left multiplication by any element preserves each summand, because $\tilde Q(\xi\tilde\Pi_\pm)=(\tilde Q\xi)\tilde\Pi_\pm$. A rank-four Clifford system must therefore use the multiplicity of the two summands: the three left multiplications generate only the rank-three system on each copy, and the fourth generator cannot be a left multiplication by the proposition above. The multiplicity is realised by two two-sided operators, the exchange $R_u$ and the grading $G$ below.

### The Swap and the Grading

Let $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ be the mixed Peirce units, with the multiplication rules

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
u=\vec\Upsilon_{+-}+\vec\Upsilon_{-+}.
$$

**Proposition.** The element $u$ satisfies $u^2=e_t$, and the right multiplication $R_u$ is an involution that exchanges $S_+$ and $S_-$. In the adapted bases $(\tilde\Pi_+,\vec\Upsilon_{-+})$ of $S_+$ and $(\vec\Upsilon_{+-},\tilde\Pi_-)$ of $S_-$, it is the identity across the two summands.

*Proof.* The square is $u^2=\vec\Upsilon_{+-}^2+\vec\Upsilon_{-+}^2+\vec\Upsilon_{+-}\vec\Upsilon_{-+}+\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_++\tilde\Pi_-=e_t$, the mixed squares vanishing. For $\xi=a\tilde\Pi_++c\vec\Upsilon_{-+}\in S_+$,

$$
\xi u=a\tilde\Pi_+u+c\vec\Upsilon_{-+}u
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

For $\xi\in S_+$, $\xi\tilde\Pi_+=\xi$ and $\xi\tilde\Pi_-=0$, so $G\xi=\xi$; for $\eta\in S_-$, $G\eta=-\eta$. The exchange gives $\tilde\Pi_+u=\vec\Upsilon_{+-}=u\tilde\Pi_-$ and $\tilde\Pi_-u=\vec\Upsilon_{-+}=u\tilde\Pi_+$. Using $R_aR_b=R_{ba}$,

$$
R_uG=R_{\tilde\Pi_+u}-R_{\tilde\Pi_-u}
=R_{u\tilde\Pi_-}-R_{u\tilde\Pi_+}=-GR_u .
$$


### The Four Generators

Define

$$
\Gamma^t=R_u,\qquad
\Gamma^k=L_{\gamma_k}G\quad(k=x,y,z).
$$

**Theorem.** The four operators $\Gamma^t,\Gamma^x,\Gamma^y,\Gamma^z$ satisfy

$$
\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}I,
$$

they are two-sided operators, and they generate $M_4(\mathbb{C})$. The root acts on the regular module $\mathbb{B}$.

*Proof.* The square of $\Gamma^t$ is $R_u^2=R_{u^2}=I$. The square of $\Gamma^k$ is $L_{\gamma_k}^2G^2=I$, because $\gamma_k^2=e_t$ and $G^2=I$. For $j\ne k$,

$$
\{\Gamma^j,\Gamma^k\}
=L_{\gamma_j\gamma_k+\gamma_k\gamma_j}G^2=0 .
$$

The mixed anticommutator is

$$
\Gamma^t\Gamma^k+\Gamma^k\Gamma^t
=R_uL_{\gamma_k}G+L_{\gamma_k}GR_u
=L_{\gamma_k}(R_uG+GR_u)=0,
$$

because left and right multiplications commute and $R_uG=-GR_u$. Hence the Clifford relations hold. The operators are two-sided:

$$
\Gamma^t=T_{e_t,u},\qquad
\Gamma^k=T_{\gamma_k,\tilde\Pi_+}-T_{\gamma_k,\tilde\Pi_-},
$$

so they lie in the enveloping algebra $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$. The sixteen monomials are independent by the Clifford relations, so they generate the whole of $M_4(\mathbb{C})$.

**The matrix frame.** In the adapted basis of the two summands,

$$
\Gamma^t=\sigma_1\otimes I_2,\qquad
\Gamma^k=\sigma_3\otimes\gamma_k,\qquad
\Gamma_5=\Gamma^t\Gamma^x\Gamma^y\Gamma^z=\sigma_2\otimes I_2 .
$$

Each generator squares to the identity, distinct generators anticommute, and $\Gamma_5$ anticommutes with all four and squares to the identity. The matrices $\sigma_1,\sigma_2,\sigma_3$ act on the multiplicity factor, and the elements $\gamma_k$ act on the simple module $S$.

**Remark (why the grading).** The swap $R_u$ commutes with every left multiplication, so it cannot anticommute with $L_{\gamma_k}$. The spatial generators of the full frame are $L_{\gamma_k}G$, not $L_{\gamma_k}$; the grading turns the commutation into anticommutation. This is the precise sense in which the fourth direction is two-sided: the three spatial generators are the left multiplications corrected by the grading, and the fourth is the exchange.

**Remark (the chiral halves are not the ideals).** The eigenspaces of $\Gamma_5$ are two-dimensional and mix $S_+$ and $S_-$; they are not left ideals. The minimal left ideals are the two copies of $S$, and the chiral projectors of $\Gamma_5$ are a different split. The distinction is the one of *The Two Chiralities of $M_4(\mathbb{C})$*, read on the regular module.

## The Unshifted Root

**Theorem.** Let

$$
\mathsf D=\sum_{\mu\in\{t,x,y,z\}}\Gamma^\mu\frac{\partial}{\partial Q_\mu}.
$$

Then $\mathsf D^2=\Box I_4$.

*Proof.* The Clifford relation gives

$$
\mathsf D^2=\frac12\sum_{\mu,\nu}\{\Gamma^\mu,\Gamma^\nu\}
\frac{\partial^2}{\partial Q_\mu\partial Q_\nu}
=\sum_\mu\frac{\partial^2}{\partial Q_\mu^2}I_4
=\Box I_4 .
$$


The operator $\mathsf D$ is a two-sided differential operator: each $\Gamma^\mu$ is a two-sided constant operator, so $\mathsf D$ is a sum of terms $T_{a,b}\partial/\partial Q_\mu$. It acts on $\mathbb{B}$-valued fields, and its square is the scalar d'Alembertian.

**The kernel at $\lambda=0$.** The equation $\mathsf D\psi=0$ is the unshifted root. In the chiral frame of §*The Chiral Form* it decouples into $D_-\psi_-=0$ and $D_+\psi_+=0$; its kernel is a chiral half of the full solution space of $\Box\psi=0$.

**Non-uniqueness.** The root is unique up to similarity, not canonical. The frame depends on the choice of the Peirce basis and of the exchange $u$; the biquaternion structure gives a canonical decomposition into the two minimal left ideals, but not a canonical matrix frame. The sign of $\Gamma_5$ and the exchange of $c$ with $-c$ give the same operator up to a change of frame.

## The Shifted D'Alembertian

### The Single Square

**Theorem.** Let $\lambda\in\mathbb{C}$ and let $c\in\mathbb{C}$ satisfy $c^2=-\lambda$. Then

$$
R_\lambda=\mathsf D+c\Gamma_5
$$

satisfies

$$
R_\lambda^2=(\Box-\lambda)I_4 .
$$

*Proof.* Every generator anticommutes with $\Gamma_5$, so $\mathsf D\Gamma_5+\Gamma_5\mathsf D=0$. Since $\Gamma_5^2=I$,

$$
R_\lambda^2=\mathsf D^2+c(\mathsf D\Gamma_5+\Gamma_5\mathsf D)+c^2\Gamma_5^2
=\Box I_4+c^2I_4=(\Box-\lambda)I_4 .
$$


**Theorem (the converse).** Every constant-coefficient root of $\Box-\lambda$ with principal symbol $\sum_\mu K_\mu\Gamma^\mu$ is of the form $R_\lambda=\mathsf D+c\Gamma_5$ with $c^2=-\lambda$, up to similarity.

*Proof.* By the root condition, $B$ anticommutes with every $\Gamma^\mu$. Then $B\Gamma_5$ commutes with every $\Gamma^\mu$, hence with the algebra they generate, which is $M_4(\mathbb{C})$. The commutant of $M_4(\mathbb{C})$ is the scalars, so $B\Gamma_5=cI$ and $B=c\Gamma_5$. The condition $B^2=-\lambda I$ gives $c^2=-\lambda$.

**The type of the shift.** The zero-order term is necessarily a multiple of the volume element; it cannot be a central scalar unless $\lambda=0$. Over $\mathbb{C}$ every $\lambda$ has a root $c$, and the two roots are opposite. If $\lambda$ is real and positive, $c$ is imaginary; if $\lambda$ is real and negative, $c$ is real. The sign of $c$ is the sign of the volume element in the frame, and it is not a separate datum.

### The Scalar Shift

**Theorem.** For every $\kappa\in\mathbb{C}$,

$$
(\mathsf D-\kappa I)(\mathsf D+\kappa I)=\Box-\kappa^2 .
$$

No single operator $\mathsf D+\kappa I$ squares to $\Box-\kappa^2$ for $\kappa\ne0$.

*Proof.* The product is $\mathsf D^2-\kappa^2I$ because $\mathsf D$ commutes with the scalar $\kappa I$. For the second statement, the cross term of $(\mathsf D+\kappa I)^2$ is $2\kappa\mathsf D$, which does not vanish for $\kappa\ne0$; equivalently, $\{\kappa I,\Gamma^\mu\}=2\kappa\Gamma^\mu\ne0$, so the anticommutator condition fails.

At $\lambda=0$, $\kappa=0$, and the two pictures coincide: $\mathsf D^2=\Box$. The scalar factorisation is a product of two first-order factors whose product is the shifted d'Alembertian; each factor alone is not a root. The single square is one first-order operator whose zero-order term anticommutes with the generators; it is a root, but its zero-order term is pseudoscalar.

### The Chiral Form

The volume element defines the chiral projectors

$$
P_+=\frac12(I+\Gamma_5),\qquad P_-=\frac12(I-\Gamma_5),
\qquad P_++P_-=I,\quad P_\pm^2=P_\pm .
$$

Because $\mathsf D$ anticommutes with $\Gamma_5$, it exchanges the two chiral halves. In the chiral basis, where $\Gamma_5=\operatorname{diag}(I_2,-I_2)$, write

$$
\mathsf D=\begin{pmatrix}0&D_-\\ D_+&0\end{pmatrix},
\qquad
D_-D_+=D_+D_-=\Box I_2 .
$$

The last identity is the chiral block form of $\mathsf D^2=\Box I_4$. The root is

$$
R_\lambda=\begin{pmatrix}cI_2&D_-\\ D_+&-cI_2\end{pmatrix}.
$$

**The two rows.** Write $\psi=(\psi_+,\psi_-)$ in the chiral decomposition. The equation $R_\lambda\psi=0$ is the pair

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

because $D_-\psi_-=\frac1cD_-D_+\psi_+=\frac1c\Box\psi_+$ and $\lambda=-c^2$. The projection $\psi\mapsto\psi_+$ is an isomorphism from $\ker R_\lambda$ onto the solution space of the shifted d'Alembertian on one chiral component; the other component is determined. The kernel of the single root is therefore a **chiral half** of the full four-component solution space. At $c=0$ the two rows decouple, $D_-\psi_-=0$ and $D_+\psi_+=0$, and the kernel is still a half.

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

**The characteristic variety.** The symbol of $R_\lambda$ is $\sum_\mu K_\mu\Gamma^\mu+c\Gamma_5$. Its determinant is $(\sum_\mu K_\mu^2-\lambda)^2$, so the first-order operator is singular exactly on the quadric $\sum_\mu K_\mu^2=\lambda$. On that quadric the symbol of $R_\lambda$ has a two-dimensional kernel, while the symbol of $\Box-\lambda$ has a four-dimensional kernel; the factor of two is the chiral half.

### The Determinant

In the chiral frame the determinant of the block matrix is

$$
\det R_\lambda
=\det(cI_2)\det\Bigl(-cI_2-\frac1cD_+D_-\Bigr)
=c^2\Bigl(-c-\frac{\Box}{c}\Bigr)^2
=(\Box-\lambda)^2 .
$$

At $\lambda=0$ this is $\det\mathsf D=\Box^2$. The same expression is the determinant of the left regular matrix of the gradient,

$$
\det\mathsf M_4(\tilde\nabla)=\langle\tilde\nabla\rangle_{\natural}^2=\Box^2 ,
$$

read on the symbol, because the determinant of the left regular matrix of an element is the square of its quaternionic norm (*$M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*). The agreement is a consistency check, not a construction: the determinant sees the square of the shifted d'Alembertian, while the kernel of the single root is a chiral half. A determinant identity is not a square root.

## The Classification of Carriers

The table classifies the carriers on which the constant-coefficient Clifford ansatz of this article can be solved. The **carrier** is the complex vector space on which the root acts; the **Clifford system** is the number of anticommuting generators available on it. The central scalar is the one-dimensional carrier $\mathbb{C}e_t$; the simple module is $S=\mathbb{B}\tilde\Pi$, of complex dimension two; the regular module is $\mathbb{B}=S_+\oplus S_-$, of complex dimension four.

| carrier | complex dimension | Clifford system | root of $\Box$ | single root of $\Box-\lambda$, $\lambda\ne0$ | scalar factorisation |
|---|---|---|---|---|---|
| $\mathbb{C}e_t$ | $1$ | none | no | no | no |
| $S=\mathbb{B}\tilde\Pi$ | $2$ | rank three | no | no | no |
| $\mathbb{B}=S_+\oplus S_-$ | $4$ | rank four | yes | yes, pseudoscalar shift | yes, scalar shift |
| $\mathbb{B}^{\oplus m}$, $m>1$ | $4m$ | rank four | yes | yes | yes, not minimal |

**The minimal carrier.** The regular module is minimal. Any larger carrier is a direct sum of copies of it, and the root acts componentwise; the Clifford system is the same rank four, and the root is not new. The simple module carries the rank-three system generated by the three $i\vec e_k$, but no rank-four system, by the dimension count. The central scalar carries none.

**The scope.** The table is a classification of the carriers of the Clifford ansatz, not a classification of all first-order operators whose square is scalar. A first-order operator with a non-Clifford principal symbol is outside the article.

## The Freedom of the Frame

The Clifford algebra $\mathbb{C}\mathrm{l}_4$ has a unique irreducible module up to isomorphism, so any two frames of the root are related by an invertible matrix:

$$
\Gamma'^\mu=S\Gamma^\mu S^{-1},\qquad B'=SBS^{-1},\qquad S\in GL_4(\mathbb{C}).
$$

The biquaternion structure does not select a canonical matrix frame. It selects the decomposition $\mathbb{B}=S_+\oplus S_-$, the exchange $u$, and the grading $G$; the adapted basis and the identification of the two summands with $S$ are choices. The volume element is canonical up to the sign of the orientation of the four generators, and the two signs of $c$ give the same operator up to the exchange $\Gamma_5\mapsto-\Gamma_5$. The root is unique up to similarity, not canonical.

**The two signs.** The sign of $c$ is the sign of the zero-order term, and it is exchanged by $\Gamma_5\mapsto-\Gamma_5$. The sign of $\Gamma_5$ is the orientation of the four generators. Neither sign changes the operator identity $R_\lambda^2=(\Box-\lambda)I$; both change the chiral decomposition and the pair of rows.

## Worked Examples

**A plane wave.** Let $\psi(Q)=\exp(\sum_\mu K_\mu Q_\mu)v$ with $v\in\mathbb{C}^4$ constant and $K_\mu\in\mathbb{C}$. Then

$$
\mathsf D\psi=\Bigl(\sum_\mu K_\mu\Gamma^\mu\Bigr)\psi,
\qquad
R_\lambda\psi=\Bigl(\sum_\mu K_\mu\Gamma^\mu+c\Gamma_5\Bigr)\psi .
$$

The first-order equation has a nonzero solution exactly when the determinant vanishes, that is on the quadric $\sum_\mu K_\mu^2=\lambda$. On the quadric the symbol has a two-dimensional kernel.

**The unshifted root on a constant spinor.** A constant $v\in\mathbb{C}^4$ satisfies $\mathsf D v=0$ and $\Box v=0$. The example shows that the root has a nontrivial kernel already at $\lambda=0$. The constant solutions of $\Box$ are all of $\mathbb{C}^4$, and $\mathsf D$ vanishes on all of them, so the constant part of the kernel does not distinguish the chiral halves; the half appears on the non-constant solutions of §*The Chiral Form*.

**Promotion of a chiral solution.** Let $\psi_+$ solve $(\Box-\lambda)\psi_+=0$ with $c\ne0$, and put $\psi_-=\frac1cD_+\psi_+$. Then

$$
D_+\psi_+=c\psi_-,\qquad
D_-\psi_-=\frac1cD_-D_+\psi_+=\frac1c\Box\psi_+=-c\psi_+,
$$

so $R_\lambda(\psi_+,\psi_-)=0$. The example exhibits the isomorphism between the kernel of the single root and the chiral half of the shifted d'Alembertian.

**The scalar factorisation.** Let $\kappa\ne0$ and let $v$ satisfy $(\sum_\mu K_\mu\Gamma^\mu-\kappa I)v=0$ for a covector $K$ with $\sum_\mu K_\mu^2=\kappa^2$. Then $(\mathsf D-\kappa I)\psi=0$ for the corresponding plane wave, and the product $(\mathsf D+\kappa I)(\mathsf D-\kappa I)\psi=0$. The other factor is obtained by $\kappa\mapsto-\kappa$. The example shows the two halves of the factorisation.

**The determinant at $\lambda=0$.** For the constant-coefficient operator $\mathsf D$, the determinant of the symbol is

$$
\det\Bigl(\sum_\mu K_\mu\Gamma^\mu\Bigr)
=\Bigl(\sum_\mu K_\mu^2\Bigr)^2=\Box^2 ,
$$

the same expression as the determinant of the left regular matrix of the gradient. At $\lambda\ne0$ the determinant is $(\Box-\lambda)^2$.

## Summary

The d'Alembertian $\Box=\partial^2/\partial Q_t^2+\Delta_Q$ is the quaternionic norm of the gradient and a scalar second-order operator. It has no first-order root on the two-dimensional simple module of $\mathbb{B}$: the three generators $i\vec e_k$ supply a rank-three Clifford system, and no fourth element of the algebra anticommutes with all three. The minimal carrier is the four-dimensional regular module $\mathbb{B}=S_+\oplus S_-$; the fourth generator is the two-sided exchange of the two minimal left ideals, and the three spatial generators are the left multiplications corrected by the grading. The unshifted root is $\mathsf D=\sum_\mu\Gamma^\mu\partial/\partial Q_\mu$, with $\mathsf D^2=\Box I$. The shifted operator $\Box-\lambda$ has a single root exactly when the zero-order term is the pseudoscalar $c\Gamma_5$ with $c^2=-\lambda$; a scalar shift admits only the factorisation $(\mathsf D-\kappa)(\mathsf D+\kappa)=\Box-\kappa^2$. The single root has a chiral half as its kernel; for $\kappa\ne0$, the scalar factorisation captures the full second-order kernel as the sum of its two first-order factors. The determinant of the single root is $(\Box-\lambda)^2$, the same expression as the determinant of the left regular matrix of the gradient at $\lambda=0$. The root is unique up to similarity, not canonical; the biquaternion structure supplies the decomposition and the exchange, not a preferred matrix frame.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | the biquaternionic gradient |
| $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial Q_\mu$ | its quaternion conjugate, $\varepsilon=(1,-1,-1,-1)$ |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$ | the d'Alembertian $\partial^2/\partial Q_t^2+\Delta_Q$ |
| $\gamma_k=i\vec e_k$ | the three Euclidean generators inside $\mathbb{B}$, $\gamma_k^2=e_t$ |
| $\Gamma^\mu$ | the four generators of the root on the regular module |
| $\Gamma_5=\Gamma^t\Gamma^x\Gamma^y\Gamma^z$ | the volume element, $\Gamma_5^2=I$ |
| $\mathsf D=\sum_\mu\Gamma^\mu\partial/\partial Q_\mu$ | the unshifted root, $\mathsf D^2=\Box I$ |
| $R_\lambda=\mathsf D+c\Gamma_5$, $c^2=-\lambda$ | the single root of $\Box-\lambda$ |
| $\kappa$, $(\mathsf D-\kappa)(\mathsf D+\kappa)$ | the scalar shift and its factorisation |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two minimal left ideals, the two copies of the simple module |
| $u=\vec\Upsilon_{+-}+\vec\Upsilon_{-+}$ | the exchange, $u^2=e_t$ |
| $R_u$, $G=R_{\tilde\Pi_+}-R_{\tilde\Pi_-}$ | the exchange operator and the grading |
| $P_\pm=\frac12(I\pm\Gamma_5)$ | the chiral projectors |

## Further Reading

- [Conventions in Mathematics](conventions-in-mathematics.html), for the derivative conventions and the gradient.
- [Biquaternion Analysis](biquaternion-analysis.html), for the gradient, its conjugate and the d'Alembertian at length.
- [The Differential Operators, the Products, the Forms and the D'Alembertian](the-differential-operators-the-products-the-forms-and-the-d-alembertian.html), for the four forms, the four norms and the definition of the d'Alembertian.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the two summands of the regular module.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the Peirce bases, the mixed units and the exchange.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the operators $T_{\tilde Q_1,\tilde Q_2}$ and their composition.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$ and the spanning theorem.
- [Bott Periodicity and the Classification](bott-periodicity-and-the-classification.html), for $\mathbb{C}\mathrm{l}_4\cong M_4(\mathbb{C})$ and the minimal module.
- [Operators on a Clifford Module](operators-on-a-clifford-module.html), for the Clifford action and the symbol.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chiral split and the distinction from the minimal left ideals.
